from django.http.response import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from .models import user_info
import hashlib

def login_view(request):
  return render(request, 'login.html')


def signup_view(request):
  return render(request, 'signup.html')


def signup_aciton(request):
  if request.method != "POST":
    return HttpResponseBadRequest('This view can not handle method {0}'.format(request.method), status=405)
  data = request.POST
  if data.get('user_pw', False) != data.get('user_pwck', False):
    return render(request, 'signup.html', {'msg': '비밀번호가 일치하지 않습니다.'})
  HashedPasswordObj =hashlib.sha1(data.get('user_pw', False).encode('UTF-8'))
  HashedPassword = HashedPasswordObj.hexdigest()
  user_info.objects.create(user_id=data.get('user_id', False), user_pw=HashedPassword, user_email=data.get('user_email', False), user_name=data.get('user_name', False))
  return render(request, 'login.html', {'msg': '회원가입 성공!'})