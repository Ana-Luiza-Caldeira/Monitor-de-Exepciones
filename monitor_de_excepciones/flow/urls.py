from django.urls import path
from flow import views

app_name = 'flow'

urlpatterns = [
    # path('search/', views.search, name="search"),
    path('', views.Index.showIndex, name="index"),

    # #flows CRUD
    # path('flow/<int:flow_id>/detail/', views.flow, name="flow"),
    # path('flow/<int:flow_id>/update/', views.update, name="update"),
    # path('flow/<int:flow_id>/delete/', views.delete, name="delete"),
    # path('flow/create/', views.create, name="create"),

    # # user
    # path('user/create/', views.register, name="register"),
    # path('user/login/', views.login_view, name="login"),
    # path('user/logout/', views.logout_view, name='logout'),
    # path('user/update/', views.user_update, name='user_update'),
]