from django.urls import path
from authorization import views

app_name = 'authorization'

urlpatterns = [
    path('authorization/login', views.login_view, name="login"),
    path('authorization/logout', views.logout, name="logout"),
]