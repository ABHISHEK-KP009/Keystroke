from django.contrib import admin
from django.urls import path, include
from . import views 
urlpatterns = [
    path('',views.home, name="home"),
    path('signup',views.signup, name="signup"),
    path('signin',views.signin, name="signin"),
    path('question1/', views.question1, name='question1'),
    path('signout',views.signout, name="signout"),
]