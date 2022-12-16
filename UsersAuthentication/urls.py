from django.urls import path
from . import views

urlpatterns = [
    path("sign-up/", views.sign_up, name="sign-up"),
    path("logout/", views.sign_out_user, name="log-out"),
    path("login/", views.log_in_user, name="login"),
    path("test/", views.testing, name="testing"),
]
