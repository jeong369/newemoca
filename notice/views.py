from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import api_view
from rest_framework.response import Response
from math import ceil

from .models import Info
from .forms import CreateForm
from .serializers import InfoSerializer, SearchInfoSerializer

# Create your views here.
def main(request) :
    
    return render(request, 'notice/main.html')

def about(request) :
    return render(request, 'notice/about.html')

def lists(request, page_pk) :
    contents = Info.objects.all().order_by('-created_at')
    print(contents)
    pagecount = ceil(len(contents)/10)
    contents_length = [x+1 for x in range(pagecount)]
    contents = contents[(page_pk-1)*10:page_pk*10]
    print(contents)
    context = {'contents' : contents, 'contents_length' : contents_length, 'pagecount' : pagecount}
    return render(request, 'notice/list.html', context)

def ox(request, page_pk) :
    info = get_object_or_404(Info, pk=page_pk)
    print(type(info.available))
    if info.available == '0' :
        info.available = '1'
        info.save()
    else :
        info.available = '0'
        info.save()
    print(info.available)
    return JsonResponse({'is_ox' : info.available, 'info_title': info.title})

def detail(request, info_pk) :
    info = get_object_or_404(Info, pk=info_pk)
    # myfile = info.file
    # fs = FileSystemStorage()
    # filename = fs.save(myfile.name, myfile)
    # uploaded_file_url = fs.url(filename)
    # 'uploaded_file_url' : uploaded_file_url
    context = {'post':info}
    return render(request, 'notice/detail.html', context)


@require_http_methods(['POST', 'GET'])
def create(request) :
    if request.user.is_staff != True :
        print("message 있음")
        messages.info(request, '관리자만 작성할 수 있습니다. 홈으로 돌아갑니다.')
        return redirect('notice:noticelists', 1)
    else :
        if request.method == "POST" :
            print(request.POST)
            info_form = CreateForm(request.POST, request.FILES)
            print(info_form)
            if info_form.is_valid() :
                print('dkdk')
                info = info_form.save(commit=False)
                print(info)
                info.title = request.POST.get('title')
                info.content = request.POST.get('content')
                info.available = request.POST.get('available')
                info.file = request.FILES.get('file')
                infom = info.save()
                print(info.title)

                getinfo = get_object_or_404(Info, title=info.title, content=info.content, available=info.available, file=info.file)
                print(getinfo)

                # myfile = request.FILES.get('file')
                # fs = FileSystemStorage()
                # filename = fs.save(myfile.name, myfile)
                # uploaded_file_url = fs.url(filename)
                # context = {'uploaded_file_url' : uploaded_file_url}
                return redirect('/notice/detail/{}'.format(getinfo.pk))
        post_form = CreateForm()
        context = {'post_form':post_form}
        return render(request, 'notice/create.html', context)

def delete(request, info_pk) :
    info = get_object_or_404(Info, pk=info_pk)
    info.delete()
    return redirect('notice:noticelists', 1)

# API
@api_view(['GET'])
def InfoGetSerializer(request) :
    users = Info.objects.all()
    serializer = InfoSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def InfoOneSerializer(request, info_pk) :
    info = get_object_or_404(Info, pk=info_pk)
    print(info)
    serializer = SearchInfoSerializer(info, many=True)
    return Response(serializer.data)