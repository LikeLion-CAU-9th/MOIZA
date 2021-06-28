from . import views
from django.urls import path

urlpatterns = [
  path('', views.kakao_login, name="kakako-login"),
  path('login/', views.login_view, name="login"),
  path('signup/', views.signup_view, name="signup"),
  path('email-check/', views.validate_mail, name="email_check"),
  path('signup-action/', views.signup_action, name="signup_action"),
  path('login-check/', views.is_login_success, name="login_check"),
]
