from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from . import models
from . import forms
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


class Login(View):
    def post(self, *args, **kwargs):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')

        if not username or not password:
            messages.error(
                self.request,
                'Invalid username or password.'
        )
            return redirect('authorization:login')
        User = authenticate(
            self.request, username=username, password=password)
        
        if not User:
            messages.error(
                self.request,
                'Invalid username or password'
        )
            return redirect('authorization:login')
        
        login(self.request, user=User)

        messages.success(
            self.request,
            'Data accepted. You are logged in the system.'
        )
        return redirect('flow:index')
    

class Logout(View):
    def get(self, *args, **kwargs):

        logout(self.request)

        return redirect('authorization:login')