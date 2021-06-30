from . import views
from django.urls import path

urlpatterns = [
  path('mainpage/', views.mainpage_view, name="mainpage"),
  path('suggestion/', views.suggestion_view, name="suggestion"),
  path('topic-complete/', views.topic_complete_view, name="topic-complete"),
  path('decision-complete/', views.decision_complete_view, name="decision-complete"),
  path('decision/<int:suggestion_seq>', views.decision_view, name="decision"),
  path('decision-preserve/', views.decision_preserve, name="decision-preserve"),
  path('decision-submit/', views.decision_submit, name="decision-submit"),
  path('decision-reason/', views.decision_reason, name="decision-reason"),
  path('other-opinion/', views.other_opinion, name="other-opinion"),
  path('disagree-reason/', views.disagree_reason, name="disagree-reason"),
  path('result/', views.result_view, name="result"),
  path('group-page/<int:group_seq>', views.grouppage_view, name="group-page"),
  path('list-page/', views.listpage_view, name="list-page"),
  path('generate-url/', views.get_hashed_url, name="gen-url"),
  path('logout-action/', views.logout_action, name="logout-action"),
  path('create-group/', views.create_group, name="create-group"),
  path('create-suggestion/', views.create_suggestion, name="create-suggestion"),
]
