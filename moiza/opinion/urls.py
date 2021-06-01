from . import views
from django.urls import path

urlpatterns = [
  path('mainpage/', views.mainpage_view, name="mainpage"),
]
