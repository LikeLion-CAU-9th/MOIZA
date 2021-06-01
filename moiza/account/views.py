from django.shortcuts import render


def login_view(request):
  return render(request, 'login.html')


def signup_view(request):
  return render(request, 'signup.html')