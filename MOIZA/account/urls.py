from . import views
from django.urls import path

urlpatterns = [
  path('login/', views.login_view, name="login"),
  path('kakalogin/', views.kaka_login, name="kakalogin"),
  path('signup/', views.signup_view, name="signup"),
  path('signup-action/', views.signup_action, name="signup_action"),
  path('login-action/', views.login_action, name="login_action"),
  path('success/', views.success_view, name="success"),
]
