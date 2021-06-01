from . import views
from django.urls import path

urlpatterns = [
  path('login/', views.login_view, name="login"),
  path('signup/', views.signup_view, name="signup"),
  path('signup-action/', views.signup_aciton, name="signup_action"),
]
