from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from . import models
# from . import forms
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logado com sucesso!')
            return redirect('flow:index')
        messages.error(request,'Login inválido')


    return render(
        request,
        'login.html',
        {
            'form': form
        }
    )

class Logout(View):
    def get(self, *args, **kwargs):

        logout(self.request)

        return redirect('authorization:login')