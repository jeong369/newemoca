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
    path('delete/<int:info_pk>/', views.delete, name="noticedelete"),
    path('update/<int:info_pk>/', views.update, name="noticeupdate"),
    path('about/', views.about),
    path('contact/', views.contact),

    
    # API Link
    path('info/', views.InfoGetSerializer),
    path('info/<int:info_pk>/', views.InfoOneSerializer, name='NoticeInfo'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)