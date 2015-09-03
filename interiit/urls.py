"""interiit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from interiit import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', views.profile_register),
    url(r'^accounts/login/', views.login_view),
    url(r'^accounts/logout/$', views.logout_view),
    url(r'^register/success/$', views.profile_register_success),
    url(r'^profile/edit/(?P<profile_id>[0-9]+)/$', views.profile_edit),
    url(r'^profile/delete/(?P<profile_id>[0-9]+)/$', views.profile_delete),
    url(r'^profile/list/$', views.profile_list)
]