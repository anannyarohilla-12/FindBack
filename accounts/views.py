from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(
                request,
                "Your FindBack account has been created!"
            )

            return redirect("home")

    else:
        form = UserCreationForm()

    return render(
        request,
        "register.html",
        {"form": form},
    )


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(
            request,
            data=request.POST,
        )

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect("home")

    else:
        form = AuthenticationForm()

    return render(
        request,
        "login.html",
        {"form": form},
    )


@login_required
def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("home")

    return redirect("home")