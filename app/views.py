# coding=utf-8

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.views.generic.base import TemplateView
from django.views.generic.list import BaseListView

from app.models import Data
from common.views import JSONResponseMixin, AjaxableCreateMixin

__author__ = 'shade'


class IndexView(TemplateView):

    template_name = 'index.html'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, request, *args, **kwargs):
        return super(IndexView, self).dispatch(request, *args, **kwargs)


class DataListView(TemplateView):

    template_name = 'data_list.html'


class UploadTextView(AjaxableCreateMixin):

    model = Data
    fields = ('fdata',)

    def dispatch(self, request, *args, **kwargs):
        return super(UploadTextView, self).dispatch(request, *args, **kwargs)


class GetTextView(JSONResponseMixin, BaseListView):

    model = Data

    def get_data(self, context):

        return [{'fdata': d.fdata, 'id': d.id} for d in context['object_list']]

