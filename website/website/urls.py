"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path
from app01 import views as app01

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', app01.index),
    path('user_list/', app01.user_list),
    re_path('user_edit/(\d)/', app01.user_edit),
    re_path('^ajax/$', app01.ajax),
    re_path('^ajax_json/$', app01.ajax_json),
    re_path('^upload/$', app01.upload),
    re_path('^upload_file/$', app01.upload_file),


]
