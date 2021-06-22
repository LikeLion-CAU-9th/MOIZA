from django.shortcuts import render

def mainpage_view(request):
  return render(request, 'mainpage.html')

def suggestion_view(request):
  return render(request, 'suggestion.html')

def topic_complete_view(request):
  return render(request, 'topic_complete.html')

def decision_complete_view(request):
  return render(request, 'decision_complete.html')

def decision_view(request):
  return render(request, 'decision.html')
