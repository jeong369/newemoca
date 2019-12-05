from django.urls import path
from . import views

app_name = 'bigfive'

urlpatterns = [
    # app
    path('', views.index, name="bigfivemain"),
    path('select/', views.select, name="bigfiveselect"),
    path('select/<int:test_num>/', views.gettest, name="bigfivegettest"),
    path('save/<int:test_pk>/<int:score_grade>/<int:user_pk>/', views.savescore, name="bigfivesavescore"),
    path('result/<int:user_pk>/<int:test_num>/', views.result, name="bigfiveresult"),
    # path('create/', views.create),
    
    # API Link
    path('test/', views.TestGetSerializer, name="getTest"),
    path('test/<int:test_pk>/', views.TestInfoSerializer, name='getTestInfo'),
    path('testtype/<int:test_num>/', views.TestTypeGetSerializer, name='getTestType'),
]