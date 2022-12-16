from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.models import auth, User
from .forms import UserForm, LoginForm
from django.contrib import messages
from django.db import connection


def sign_up(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            User.objects.create_user(
                username=username, first_name=first_name, last_name=last_name, email=email, password=password)
            authentication = auth.authenticate(request, username=username, email=email, password=password)
            if authentication is not None:
                auth.login(request, authentication)
            return HttpResponseRedirect(reverse("home"))
        else:
            messages.error(request, str(form.errors))
            return HttpResponseRedirect(reverse("sign-up"))
    else:
        form = UserForm()
    return render(request, "auth/create-account.html", {"request": request, "form": form})


def sign_out_user(request):
    auth.logout(request)
    return redirect("home")


def log_in_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            username = form.cleaned_data["username"]
            authentication = auth.authenticate(request, username=username, email=email, password=password)
            if authentication is not None:
                auth.login(request, authentication)
                return HttpResponseRedirect(reverse("home"))
            else:
                HttpResponse("Invalid credentials")
        else:
            return HttpResponse(f"Error {str(form.errors)}")
    else:
        form = LoginForm()
    return render(request, "auth/login.html", {"request": request, "form": form})


def testing(request):
    cursor = connection.cursor()
    cursor.execute("""DELETE FROM "auth_user";""")
    return HttpResponse("success %s " % str(request))
