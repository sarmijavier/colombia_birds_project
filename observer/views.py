""" Observer views. """

#Django
from django.views.generic.base import TemplateView


class MyView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        return context
    