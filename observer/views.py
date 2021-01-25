""" Observer views. """

#Django
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views


class MyView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        return context


class LoginView(auth_views.LoginView):
    """ Login View. """
    template_name = 'observer/login.html'
    redirect_authenticated_user = True


    