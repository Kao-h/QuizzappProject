from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('',  views.home, name='home'),
    path('home/', views.home, name='home'),
    path('try/', views.try_it, name='try_it'),
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('quizz/', views.quizz, name='quizz'),
    path('quizz/microscopy/', views.microscopy, name='microscopy'),
    path('quizz/biological/', views.biological, name='biological'),
    path('quizz/explore/', views.explore, name='explore')
]
