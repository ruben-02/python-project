from django.contrib import admin
from django.urls import path
#from django.conf.urls import url
from django.urls import path, re_path

from StudentApp import views

urlpatterns = [
    re_path(r'^student$',views.studentApi),
    re_path(r'^student$',views.studentApi),
    re_path(r'^student/([0-9]+)$',views.studentApi),
    path('admin/', admin.site.urls),
]