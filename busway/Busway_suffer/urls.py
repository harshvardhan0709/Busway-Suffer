from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path

urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('adminbus.urls',namespace='adminbus')),
    url(r'^api/users/', include("accounts.api.urls", namespace='users-api')),
]
