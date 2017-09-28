# coding=utf-8

from django.contrib import admin
from django.contrib.auth.models import Group, User

from app.models import Data

__author__ = 'shade'


@admin.register(Data)
class DataAdmin(admin.ModelAdmin):

    list_display = ('id', 'fdata',)
    list_display_links = list_display


admin.site.unregister(Group)
admin.site.unregister(User)