# coding=utf-8
import json

from django.http.response import JsonResponse
from django.views.generic.edit import CreateView

__author__ = 'shade'


class JSONResponseMixin(object):

    def render_to_json_response(self, context, **response_kwargs):
        return JsonResponse(self.get_data(context), safe=False, **response_kwargs)

    def get_data(self, context):
        raise NotImplementedError

    def render_to_response(self, context):
        return self.render_to_json_response(context)


class AjaxableCreateMixin(CreateView):

    def get_form_kwargs(self):

        kwargs = super(AjaxableCreateMixin, self).get_form_kwargs()
        kwargs.update(json.loads(self.request.body.decode()))

        return kwargs

    def form_invalid(self, form):
        return JsonResponse(form.errors, status=400)

    def form_valid(self, form):
        super(AjaxableCreateMixin, self).form_valid(form)
        return JsonResponse({'created': True})

    def get_success_url(self):
        return '/'
