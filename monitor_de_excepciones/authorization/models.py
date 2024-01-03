from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from flow.models import Flow


class Cargo(models.Model):

    name = models.CharField(max_length=50, null=True)
    usuario = models.ManyToManyField(User, related_name='roles')

    def __str__(self):
        return self.name


class Autorization(models.Model):
    
    flowAuth = models.ForeignKey(Flow, on_delete=models.CASCADE, null=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
