from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.http import HttpResponse
from . import models
from . import forms
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from flow.models import Flow, Notification
from .forms import FlowForm
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
    def newFlow(request):
        if request.method == 'POST':
            form = FlowForm(request.POST)
            if form.is_valid():
                new_flow = form.save(commit=False)
                new_flow.owner = request.user
                new_flow.save()
                return redirect('flow:home')
            else:
                form = FlowForm()
            
            return render(request, 'flow:home', {'form': form})

class EditFlow(DispatchLoginRequiredMixin, View):
    def editFlow(request, id_processo):
        flow = get_object_or_404(Flow, pk=id_processo, show=True, owner=request.user)
        form_action = reverse('flow:edit', args=(id_processo))

        if request.method == 'POST':
            form = FlowForm(request.POST, request.FILES, instance=flow)

            context = {'form': form, 'form_action': form_action}

            if form.is_valid():
                update_flow = form.save()
                return redirect('flow:edit', id_processo=update_flow.pk)
            
            return render(request, 'flow:home', context)

class CheckNotif(DispatchLoginRequiredMixin, View):
    pass

class AddNotif(DispatchLoginRequiredMixin, View):
    pass

class EditNotif(DispatchLoginRequiredMixin, View):
    pass


