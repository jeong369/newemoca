from django.urls import path
from . import views

app_name = 'bigfive'

urlpatterns = [
    # app
    path('create/', views.create),
    
    # API Link
    # path('test/', views.TestGetSerializer),
    # path('test/<int:test_pk>/', views.TestInfoSerializer, name='getTest'),
]