from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

class Flow(models.Model):

    id_processo = models.CharField(max_length=50)
    module = models.CharField(max_length=50)
    organization = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    state = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        
        verbose_name='Flow'
        verbose_name_plural='Flows'
        unique_together = ('id_processo', 'module', 'organization')
    
    def __str__(self):
        return f'{self.id_processo} - {self.module} - {self.organization}'


class Notification(models.Model):

    flow = models.ForeignKey(Flow, on_delete=models.CASCADE)
    id_transacao = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    state = models.BooleanField(default=True)
    reprocessavel = models.BooleanField(default=False)
    gerenciavel = models.BooleanField(default=False)

    class Meta:
        
        verbose_name='Notification'
        verbose_name_plural='Notifications'

    def __str__(self):
        return f'{self.flow} - {self.id_transacao}'


class OriginCon(models.Model):

    notif = models.ForeignKey(Notification, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)
    protocol = models.CharField(max_length=50)
    url = models.URLField()
    idOrigin = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.notif} - {self.tipo}'
    

class DestinyCon(models.Model):

    notif = models.ForeignKey(Notification, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)
    protocol = models.CharField(max_length=50)
    url = models.URLField()
    idDestiny = models.CharField(max_length=50)
#    ociiD_objectStorage = 
#    ociiD_file = 
    
    def __str__(self):
        return f'{self.notif} - {self.tipo}'


class Data(models.Model):
    

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Campo(models.Model):

    name = models.ForeignKey(Data, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)
    pesquisavel = models.BooleanField(default=False)
    editavel = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - {self.tipo}'
    

class Regras(models.Model):

    campo = models.ForeignKey(Campo, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)
    descricao = models.TextField
    prompt = models.CharField(max_length=50)

    class Meta:
        
        verbose_name='Regra'
        verbose_name_plural='Regras'


    def __str__(self):
        return f'{self.campo} - {self.tipo}'

