from django.shortcuts import render
import opinion.views

# Create your views here.
def mainpage_view(request):
    return render(request, 'mainpage.html')

def grouppage_view(request):
    return render(request, 'grouppage.html')

def listpage_view(request):
    return render(request, 'listpage.html')

def suggestion_view(request):
  return render(request, 'suggestion.html')


def topic_complete_view(request):
  return render(request, 'topic_complete.html')


def decision_complete_view(request):
  return render(request, 'decision_complete.html')


def decision_view(request):
  return render(request, 'decision.html')

def decision_reason(request):
  return render(request, 'decision_reason.html')

def other_opinion(request):
  return render(request, 'other_opinion.html')

def disagree_reason(request):
  return render(request, 'disagree_reason.html')

def result_view(request):
  return render(request, 'result.html')
