from django.urls import path
from .views import *

urlpatterns = [
    path("", Index, name="home"),
    path("register/", SignUp, name="register"),
    path("login/", SignIn, name="login"),
    path("logout/", Logout, name="logout"),
    path("reset/", ResetPassword, name="reset"),
]