from django.shortcuts import render
from .forms import SignUpForm
from .models import User
from .utilities import get_date
from django.contrib.auth import login
from django.http import HttpResponse


def index(request):
    return render(request, 'home/index.html')


def log_in(request):
    return render(request, 'home/log-in.html')


# def sign_up(request):
#     return render(request, 'home/sign-up.html')


def sign_up(request):
    print("inside sign_up")
    if request.method == "POST":
        print("inside reqest==post")
        form = SignUpForm(data=request.POST)

        # print("inside form is valid")
        name = request.POST.get('name', '')
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        confirm_email = request.POST.get('confirm_email', '')
        password = request.POST.get('password', '')
        month = request.POST.get('month', '')
        day = request.POST.get('day', '')
        year = request.POST.get('year', '')
        gender = request.POST.get('gender', '')

        user = User.objects.create_user(username=username, email=email, password=password,
                                        date_of_birth=get_date(day, month, year), gender=gender,
                                        first_name=name)
        login(request, user)

        return HttpResponse("<h1> Welcome new user </h1>")

    else:
        print("inside else")
        form = SignUpForm()
        return render(request, 'home/sign-up.html', {'form': form})


def password_reset(request):
    return render(request, 'home/password-reset.html')

