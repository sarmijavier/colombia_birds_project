""" Observer models. """


#Django
from django.contrib.auth.models import User
from django.db import models



class Observer(models.Model):

    """ Observer model. """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=200, blank=True)
    picture = models.ImageField(upload_to='observers/pictures', height_field=192, width_field=288, blank=True)
    
    create = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)