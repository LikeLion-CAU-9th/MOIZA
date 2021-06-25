from . import views
from django.urls import path

urlpatterns = [
  path('', views.login_view, name="login"),
  path('signup/', views.signup_view, name="signup"),
  path('email-check/', views.validate_mail, name="email_check"),
  path('signup-action/', views.signup_action, name="signup_action"),
  path('login-action/', views.login_action, name="login_action"),
  path('success/', views.success_view, name="success"),
]
