from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # app
    path('create/', views.create, name="accountscreate"),
    
    # API Link
    path('user/', views.UserGetSerializer),
    path('user/<int:user_pk>/', views.UserInfoSerializer, name='UserInfo'),
]