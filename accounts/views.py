from django.contrib.auth import (
	authenticate, get_user_model,
	login, logout,
	)
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm

from django.contrib.auth.models import User

# Create your views here.

def login_view(request):
	print(request.user.is_authenticated())
	title = "Login"
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		login(request, user)

	return render(request, "login.html", {"form":form, "title":title})

def register_view(request):
	if request.method=='POST':
		form=UserRegisterForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(
				username = form.cleaned_data.get("username"),
				password = form.cleaned_data.get("password1"),
				email = form.cleaned_data.get("email")
				)
			password = form.cleaned_data.get("password1")
			new_user = authenticate(username=user.username, password=password)
			login(request,new_user)
			return redirect("/posts/")
		
		return render(request, "register.html", {"form":form})
		


		

		


def logout_view(request):
	logout(request)
	return render(request, "logout.html", {})