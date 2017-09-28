# coding=utf-8

from .views import *
from django.conf.urls import url

__author__ = 'shade'


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^list$', DataListView.as_view(), name='list'),
    url(r'^uploadText$', UploadTextView.as_view(), name='uploadText'),
    url(r'^getText$', GetTextView.as_view(), name='getText'),

]