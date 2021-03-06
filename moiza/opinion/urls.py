from . import views
from django.urls import path

urlpatterns = [
  path('mainpage/', views.mainpage_view, name="mainpage"),
  path('suggestion/', views.suggestion_view, name="suggestion"),
  path('topic-complete/', views.topic_complete_view, name="topic-complete"),
  path('decision-complete/', views.decision_complete_view, name="decision-complete"),
  path('decision/', views.decision_view, name="decision"),
  path('decision-reason/', views.decision_reason, name="decision-reason"),
  path('other-opinion/', views.other_opinion, name="other-opinion"),
  path('disagree-reason/', views.disagree_reason, name="disagree-reason"),
  path('result/', views.result_view, name="result"),
  path('group-page/', views.grouppage_view, name="group-page"),
  path('list-page/', views.listpage_view, name="list-page"),
]
