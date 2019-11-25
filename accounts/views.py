from django.shortcuts import render, get_object_or_404
from .models import User
from .forms import CreateForm
# serailizers
from .serializers import UserSerializer, SearchUserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response



# Create your views here.

# 닉네임으로 회원가입(닉네임 중복 가능)
def create(request) :
    if request.method == "POST" :
        print(request.POST)
        user_form = CreateForm(request.POST)
        if user_form.is_valid() :
            user = user_form.save(commit=False)
            user.name = request.POST.get('name')
            user.age = request.POST.get('age')
            user.gender = request.POST.get('gender')
            user = user.save()
        return render(request, 'accounts/create.html')
    
    return render(request, 'accounts/create.html')





# API
@api_view(['GET'])
def UserGetSerializer(request) :
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def UserInfoSerializer(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    print(user)
    serializer = SearchUserSerializer(user, many=True)
    return Response(serializer.data)