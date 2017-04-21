from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')


def log_in(request):
    return render(request, 'home/log-in.html')


def sign_up(request):
    return render(request, 'home/sign-up.html')


def password_reset(request):
    return render(request, 'home/password-reset.html')

