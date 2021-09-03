from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.registration, name="registration"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout")
]