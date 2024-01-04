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
from .forms import FlowForm, NotificationForm
from authorization.models import Authorization

class DispatchLoginRequiredMixin(View):
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('authorization:login')
        
        return super().dispatch(*args, **kwargs)
    
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(User=self.request.user)
        return qs

class Index(DispatchLoginRequiredMixin, View):
    def showIndex(request):
        print(request)
        # verificar a autorizacao antes!
        # single_authorization = get_object_or_404(Authorization.objects.filter(process_id=process_id, module=module, organization=organization))

        # if single_authorization.user == request.user:
        #     single_flow = get_object_or_404(Flow.objects.filter(process_id=process_id, module=module, organization=organization)) #tratamento caso houver erro

        #     site_title = f'{single_flow.module} - {single_flow.organization}'

        context = {
            # 'flow': single_flow,
            # 'site_title': site_title,
        }

        return render(request, 'index.html', context)

class CheckFlow(DispatchLoginRequiredMixin, View):
    def showFlow(self, *args, **kwargs):
        validate = Flow.objects.filter(owner=self.user)

        context = {
            'flows': validate
        }

        return render(self.request, 'flow/home.html', context)

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
    def editFlow(request, process_id):
        flow = get_object_or_404(Flow, pk=process_id, show=True, owner=request.user)
        form_action = reverse('flow:edit', args=(process_id))

        if request.method == 'POST':
            form = FlowForm(request.POST, request.FILES, instance=flow)

            context = {'form': form, 'form_action': form_action}

            if form.is_valid():
                update_flow = form.save()
                return redirect('flow:edit', process_id=update_flow.pk)
            
            return render(request, 'flow:home', context)

class CheckNotif(DispatchLoginRequiredMixin, View):
    def showNotif(self, *args, **kwargs):
        validate = Notification.objects.filter(owner=self.user)

        context = {
            'notifs': validate
        }

        return render(self.request, 'flow/home.html', context)  

class AddNotif(DispatchLoginRequiredMixin, View):
    def newNotification(request):
        if request.method == 'POST':
            form = NotificationForm(request.POST)
            if form.is_valid():
                new_notification = form.save(commit=False)
                new_notification.owner = request.user
            #   new_notification.flow = 
                new_notification.save()
                return redirect('flow:home')
            else:
                form = NotificationForm()
            
            return render(request, 'flow:home', {'form': form})

class EditNotif(DispatchLoginRequiredMixin, View):
    def editNotif(request, transaction_id):
        notif = get_object_or_404(Flow, pk=transaction_id, show=True, owner=request.user)
        form_action = reverse('flow:edit', args=(transaction_id))

        if request.method == 'POST':
            form = NotificationForm(request.POST, request.FILES, instance=notif)

            context = {'form': form, 'form_action': form_action}

            if form.is_valid():
                update_notif = form.save()
                return redirect('flow:edit', transaction_id=update_notif.pk)
            
            return render(request, 'flow:home', context)


