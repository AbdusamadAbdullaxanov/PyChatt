from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import MessagesModel
from django.db import connection
from .forms import TestForm


def homepage(request):
    print(request.user.is_authenticated)
    return render(request, 'Home.html', {})


def delete_message(request, pk):
    print(request)
    model_to_delete = MessagesModel.objects.get(id=pk)
    chat_id = model_to_delete.user_to_id
    model_to_delete.delete()
    return redirect("chat", chat_id)


def friends(request):
    if request.user.is_authenticated:
        users = User.objects.all()
        return render(request, "messages/chat-form.html", {"request": request, "users": users})
    else:
        return redirect("login")


def chat_with_friend(request, pk):
    one_to_one = [request.user.id, pk]
    messages = MessagesModel.objects.filter(user_id__in=one_to_one).filter(user_to_id__in=one_to_one).values()
    print(request.user.id, 9 * "\n")
    if request.method == "POST":
        form = TestForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data["message"]
            MessagesModel(message=message, user_id=request.user.id, user_to_id=pk, username=request.user.username).save()
            return redirect("chat", pk)
    else:
        form = TestForm()
    return render(request, "messages/private-chat.html", {"request": request, "form": form, "messages": messages, "pk": pk})


def user_info(request, pk):
    user = User.objects.get(id=pk)
    return render(request, "auth/user-info.html", {"request": request, "user": user})


def search_users(request):
    if request.method == "POST":
        search_user = request.POST.get("user")
        profiles = User.objects.filter(username__icontains=search_user).values()
    else:
        profiles = ""
    return render(request, "auth/searched-users.html", {"request": request, "profiles": profiles})


def test(request):
    print(request)
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS table_name_01 ("name" TEXT)""")
    connection.commit()
    return HttpResponseRedirect("https://www.youtube.com")
