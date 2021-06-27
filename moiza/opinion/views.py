from django.shortcuts import get_object_or_404, render,redirect
from opinion.models import Suggestion, Selection

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

def selection_write(request, pk):
        selection = Selection()
        selection.selection_contents = request.POST.get('content')
        selection.save()
        return redirect('/post/'+str(pk))

def decision_reason(request):
  return render(request, 'decision_reason.html')

def other_opinion(request):
  return render(request, 'other_opinion.html')

def disagree_reason(request):
  return render(request, 'disagree_reason.html')

def result_view(request):
  return render(request, 'result.html')
