"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import re_path, path, include
from website.views import hello, current_datetime, hours_ahead
from website import views


urlpatterns = [
    re_path('^home/$', views.home, name='home'),
    re_path('^time/$', current_datetime),
    re_path(r'^time/plus/(\d{1,2})/$', hours_ahead),
    #re_path(r'^search-form', views.search_form),
    #re_path(r'^search/$', views.search),
    path('admin/', admin.site.urls),
    re_path('^home/add', views.add, name='add'),
]
