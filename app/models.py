# coding=utf-8

from django.db import models

__author__ = 'shade'



class Data(models.Model):

    fdata = models.TextField('Строка')