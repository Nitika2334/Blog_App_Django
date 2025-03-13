from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.blog, name="blog-home"),
    path('about/', views.about , name= "blog-about"),
]