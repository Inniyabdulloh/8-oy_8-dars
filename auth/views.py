from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


class RegisterView(View):
    def get(self, request):
        return render(request, 'auth/register.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username=username)
            user.set_password(password)
            user.save()
        except:
            messages.warning(request, 'Nimadir xato')
            return redirect('register')
        return redirect('login')


class LoginView(View):
    def get(self, request):
        return render(request, 'auth/login.html')
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            return redirect('register')