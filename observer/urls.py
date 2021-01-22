""" Observer urls. """


#Django
from django.urls import path

#views
from observer.views import MyView

urlpatterns = [
    
    path(
        route='login/',
        view=MyView.as_view(),
        name='login'
    ),
]
