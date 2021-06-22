from . import views
from django.urls import path

urlpatterns = [
  path('mainpage/', views.mainpage_view, name="mainpage"),
  path('grouppage/', views.grouppage_view, name="grouppage"),
  path('listpage/', views.listpage_view, name="listpage"),
]
