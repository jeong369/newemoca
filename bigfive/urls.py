from django.urls import path
from . import views

app_name = 'bigfive'

urlpatterns = [
    # app
    path('', views.index, name="bigfivemain"),
    path('select/', views.select, name="bigfiveselect"),
    path('select/<int:test_num>/', views.gettest, name="bigfivegettest"),
    path('select/<int:test_pk>/<int:score_grade>/', views.savescore, name="bigfivesavescore"),
    # path('create/', views.create),
    
    # API Link
    # path('test/', views.TestGetSerializer),
    # path('test/<int:test_pk>/', views.TestInfoSerializer, name='getTest'),
]