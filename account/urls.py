from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls'), name='login'),
    path('', include('django.contrib.auth.urls'), name='logout'),
    path('', include('django.contrib.auth.urls'), name='logout_then_login'),
    path('', views.table, name='table'),
    path('register/', views.register, name='register'),
    path('table/', views.userlist, name='table')
]



