from django.conf.urls import url
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'adminbus'

urlpatterns = [
    url(r'^$', views.mainpage , name='user'),
    url(r'^login/$', views.login, name='login'),
    url(r'^(?P<menu>[\s\w]+)/$', views.userprofile , name='userprofile'),
]
