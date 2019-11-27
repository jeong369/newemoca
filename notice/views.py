from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from django.contrib import messages

from .models import Info
from .forms import CreateForm

# Create your views here.
def main(request) :
    
    return render(request, 'notice/main.html')

def about(request) :
    return render(request, 'notice/about.html')

def lists(request) :
    contents = Info.objects.all()
    contents_length = str(len(contents))
    print(contents_length)
    context = {'contents' : contents, 'contents_length' : contents_length}
    return render(request, 'notice/list.html', context)

def detail(request, info_pk) :
    info = get_object_or_404(Info, pk=info_pk)
    context = {'post':info}
    return render(request, 'notice/detail.html', context)

@require_http_methods(['POST', 'GET'])
def create(request) :
    if request.user.is_staff != True :
        print("message 있음")
        messages.info(request, '관리자만 작성할 수 있습니다. 홈으로 돌아갑니다.')
        return redirect('notice:noticelists')
    else :
        if request.method == "POST" :
            print(request.POST)
            info_form = CreateForm(request.POST)
            print(info_form)
            if info_form.is_valid() :
                info = info_form.save(commit=False)
                info.title = request.POST.get('title')
                info.content = request.POST.get('content')
                info = info.save()

                return redirect('notice:noticelists')
        return render(request, 'notice/create.html')