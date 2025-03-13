"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include(blog.urls)),   
    #call : localhost:8000/blog/home/ - it will cut the part here that matches here will send the rest of the part to the url of the app [i.e. - home/]
    # [why / ?] - because we will not keep the forward slash it will redirect to the path without the forward slash from the project
    #we can leave it empty to make it the default route for the 8000 port or local host 
] 
