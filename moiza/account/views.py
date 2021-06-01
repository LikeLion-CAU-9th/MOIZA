from django.http.response import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from .models import user_info
import hashlib

def login_view(request):
  return render(request, 'login.html')


def signup_view(request):
  return render(request, 'signup.html')


def signup_action(request):
  if request.method != "POST":
    return HttpResponseBadRequest('This view can not handle method {0}'.format(request.method), status=405)
  data = request.POST
  if validate_id(request, data.get('user_id', False)) == False:
    return render(request, 'signup.html', {'msg_id': '이미 가입된 아이디입니다.'})
  if data.get('user_pw', False) != data.get('user_pwck', False):
    return render(request, 'signup.html', {'msg_pw': '비밀번호가 일치하지 않습니다.'})
  if validate_mail(request, data.get('user_email', False)) == False:
    return render(request, 'signup.html', {'msg_mail': '이미 가입된 이메일입니다.'})
  HashedPasswordObj =hashlib.sha1(data.get('user_pw', False).encode('UTF-8'))
  HashedPassword = HashedPasswordObj.hexdigest()
  user_info.objects.create(user_id=data.get('user_id', False), user_pw=HashedPassword, user_email=data.get('user_email', False), user_name=data.get('user_name', False))
  return render(request, 'login.html', {'msg': '회원가입 성공!'})


def validate_id(request, id):
  queryset = user_info.objects.filter(user_id = id)
  if len(queryset) > 0:
    return False
  return True


def validate_mail(request, email):
  queryset = user_info.objects.filter(user_email = email)
  if len(queryset) > 0:
    return False
  return True