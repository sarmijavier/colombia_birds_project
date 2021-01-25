""" Observer urls. """


#Django
from django.urls import path

#views
from observer.views import LoginView, MyView

urlpatterns = [
    
    path(
        route='login/',
        view=LoginView.as_view(),
        name='login'
    ),
    path(
        route='main/',
        view=MyView.as_view(),
        name='main'
    )
]
