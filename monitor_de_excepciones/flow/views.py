from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from . import models
from . import forms
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from flow.models import Flow, Notification
from authorization.models import Autorization

class DispatchLoginRequiredMixin(View):
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('authorization:login')
        
        return super().dispatch(*args, **kwargs)
    
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(User=self.request.user)
        return qs

class CheckFlow(DispatchLoginRequiredMixin, View):
    def showFlow(self, *args, **kwargs):
        validate = Flow.objects.filter()

class AddFlow(DispatchLoginRequiredMixin, View):
    pass

class EditFlow(DispatchLoginRequiredMixin, View):
    pass

class CheckNotif(DispatchLoginRequiredMixin, View):
    pass

class AddNotif(DispatchLoginRequiredMixin, View):
    pass

class EditNotif(DispatchLoginRequiredMixin, View):
    pass


