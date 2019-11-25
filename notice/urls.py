from django.urls import path
from . import views

app_name = 'notice'

urlpatterns = [
    # app
    path('', views.lists, name="noticelists"),
    path('create/', views.create, name="noticecreate"),
    
    # API Link
    # path('user/', views.UserGetSerializer),
    # path('user/<int:user_pk>/', views.UserInfoSerializer, name='UserInfo'),
]