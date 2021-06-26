from django.shortcuts import get_object_or_404, render,redirect
from opinion.models import Suggestion, Opinion

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

def opinion_write(request, pk):
        opinion = Opinion()
        opinion.opinion_contents = request.POST.get('content')
        opinion.save()
        return redirect('/post/'+str(pk))