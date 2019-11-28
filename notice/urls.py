from django.urls import path
from . import views

app_name = 'notice'

urlpatterns = [
    # app
    path('', views.main, name="main"),
    path('lists/<int:page_pk>/', views.lists, name="noticelists"),
    path('create/', views.create, name="noticecreate"),
    path('detail/<int:info_pk>/', views.detail, name="noticedetail"),
    path('lists/<int:page_pk>/available/', views.ox, name="noticeox"),
    path('about/', views.about),
    
    # API Link
    path('info/', views.InfoGetSerializer),
    path('info/<int:info_pk>/', views.InfoOneSerializer, name='NoticeInfo'),
]