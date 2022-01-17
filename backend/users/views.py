from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpRequest
from .forms import UserForm


def log_out(request: HttpRequest):
    logout(request)
    return redirect("listings:index")


def register(request: HttpRequest):
    if request.method != "POST":
        form = UserForm()
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users:login")

    context = {"form": form}
    return render(request, "registration/register.html", context)
