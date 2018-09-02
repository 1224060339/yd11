from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^login/$',login_views),
    url(r'^register/$',register_views),
    url(r'^01_login/$',login1_views),
    url(r'^02_login/$',login2_views),
    url(r'^03_login/$',login3_views),
    ]