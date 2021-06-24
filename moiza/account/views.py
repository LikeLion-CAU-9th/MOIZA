from django.http.response import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from .models import user_info
import hashlib

def login_view(request):
  return render(request, 'login.html')


def signup_view(request):
  return render(request, 'signup.html')


def success_view(request):
  return render(request, 'success.html')


def login_action(request):
  data = request.GET
  login_success = is_login_available(request, data.get('id', False), data.get('pw', False))
  
  if login_success == False:
    return HttpResponse("False")
  is_session_success = session_attach(request, data.get('input_id', False))
  if is_session_success == False:
    return HttpResponseBadRequest('Session is not attached!', status=500)
  return HttpResponse("True")
  

def is_login_available(request, id, raw_pw):
  HashedPasswordObj =hashlib.sha1(raw_pw.encode('UTF-8'))
  HashedPassword = HashedPasswordObj.hexdigest()
  queryset = user_info.objects.filter(user_id = id, user_pw = HashedPassword)
  if len(queryset) == 1:
    return True
  return False


def session_attach(request, user_id):
  request.session['user_id'] = user_id
  return ('user_id' in request.session)


def signup_action(request):
  if request.method != "POST":
    return HttpResponseBadRequest('This view can not handle method {0}'.format(request.method), status=405)
  data = request.POST
  HashedPasswordObj =hashlib.sha1(data.get('user_pw', False).encode('UTF-8'))
  HashedPassword = HashedPasswordObj.hexdigest()
  user_info.objects.create(user_id=data.get('user_id', False), user_pw=HashedPassword, user_email=data.get('user_email', False), user_name=data.get('user_name', False))
  return render(request, 'login.html')


def validate_mail(request):
  email = request.GET['email']
  queryset = user_info.objects.filter(user_email = email)
  print(queryset)
  print(len(queryset))
  if len(queryset) > 0:
    return HttpResponse('False')
  return HttpResponse('True')