from django.http.response import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from .models import User_info
import hashlib


def login_view(request):
  session_existence = authorization(request)
  if session_existence:
    return redirect('mainpage')
  return render(request, 'login.html')


def kakao_login(request):
  session_existence = authorization(request)
  if session_existence:
    return redirect('mainpage')
  return render(request, 'kakalogin.html')


def signup_view(request):
  session_existence = authorization(request)
  if session_existence:
    return redirect('mainpage')
  return render(request, 'signup.html')


def is_login_success(request):
  data = request.GET
  email = data.get('email', False)
  login_success = is_login_available(request, email, data.get('pw', False))
  if login_success == False:
    return HttpResponse("False")
  is_session_success = session_attach(request, email)
  if is_session_success == False:
    return HttpResponseBadRequest('Session is not attached!', status=500)
  return HttpResponse("True")
  

def is_login_available(request, email, raw_pw):
  print("Email: ", email)
  print("Pw: ", raw_pw)
  HashedPasswordObj =hashlib.sha1(raw_pw.encode('UTF-8'))
  HashedPassword = HashedPasswordObj.hexdigest()
  queryset = User_info.objects.filter(user_email = email, user_pw = HashedPassword)
  print("Q Len: ", len(queryset))
  if len(queryset) == 1:
    return True
  return False


def session_attach(request, user_email):
  request.session['user_email'] = user_email
  return ('user_email' in request.session)


def signup_action(request):
  if request.method != "POST":
    return HttpResponseBadRequest('This view can not handle method {0}'.format(request.method), status=405)
  data = request.POST
  HashedPasswordObj =hashlib.sha1(data.get('user_pw', False).encode('UTF-8'))
  HashedPassword = HashedPasswordObj.hexdigest()
  User_info.objects.create(user_email=data.get('user_email', False), user_pw=HashedPassword, user_name=data.get('user_name', False))
  return redirect('login')


def validate_mail(request):
  email = request.GET['email']
  queryset = User_info.objects.filter(user_email = email)
  print(queryset)
  print(len(queryset))
  if len(queryset) > 0:
    return HttpResponse('False')
  return HttpResponse('True')


def authorization(request):
  return ('user_email' in request.session)