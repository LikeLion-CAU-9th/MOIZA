from . import views
from django.urls import path

urlpatterns = [
  path('mainpage/', views.mainpage_view, name="mainpage"),
  path('suggestion/', views.suggestion_view, name="suggestion"),
  path('topic-complete/', views.topic_complete_view, name="topic-complete"),
  path('decision-complete/', views.decision_complete_view, name="decision-complete"),
  path('decision/', views.decision_view, name="decision"),
]
