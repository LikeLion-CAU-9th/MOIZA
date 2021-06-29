from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from opinion.models import Suggestion, Selection

# Create your views here.
def mainpage_view(request):
  # authorize_action(request)
  session_existence = authorization(request)
  if not session_existence:
    return redirect('login')
  return render(request, 'mainpage.html')


def grouppage_view(request):
  # authorize_action(request)
  session_existence = authorization(request)
  if not session_existence:
    return redirect('login')
  return render(request, 'grouppage.html')


def listpage_view(request):
  # authorize_action(request)
  session_existence = authorization(request)
  if not session_existence:
    return redirect('login')
  return render(request, 'listpage.html')


def suggestion_view(request):
  # authorize_action(request)
  session_existence = authorization(request)
  if not session_existence:
    return redirect('login')
  return render(request, 'suggestion.html')


def topic_complete_view(request):
  # authorize_action(request)
  session_existence = authorization(request)
  if not session_existence:
    return redirect('login')
  return render(request, 'topic_complete.html')


def decision_complete_view(request):
  # authorize_action(request)
  session_existence = authorization(request)
  if not session_existence:
    return redirect('login')
  return render(request, 'decision_complete.html')


def decision_view(request):
  # authorize_action(request)
  session_existence = authorization(request)
  if not session_existence:
    return redirect('login')
  return render(request, 'decision.html')


def selection_write(request):
  # authorize_action(request)
  session_existence = authorization(request)
  if not session_existence:
    return redirect('login')
  if request.method == "POST":
    selection = Selection()
    selection.suggestion = get_object_or_404(Suggestion)
    selection.selection_contents = request.POST.get('content')
    selection.save()
    return redirect('/decision-complete/')


def decision_reason(request):
  # authorize_action(request)
  session_existence = authorization(request)
  if not session_existence:
    return redirect('login')
  return render(request, 'decision_reason.html')


def other_opinion(request):
  # authorize_action(request)
  session_existence = authorization(request)
  if not session_existence:
    return redirect('login')
  return render(request, 'other_opinion.html')


def disagree_reason(request):
  # authorize_action(request)
  session_existence = authorization(request)
  if not session_existence:
    return redirect('login')
  return render(request, 'disagree_reason.html')


def result_view(request):
  # authorize_action(request)
  session_existence = authorization(request)
  if not session_existence:
    return redirect('login')
  return render(request, 'result.html')


def logout_action(request):
  session_existence = authorization(request)
  if session_existence:
    del request.session['user_email']
    return HttpResponse('True')
  return HttpResponse('False')

def opinion_write(request):
  pass


def authorization(request):
  return ('user_email' in request.session)


def authorize_action(request):
  session_existence = authorization(request)
  print("sess", session_existence)
  if not session_existence:
    return redirect('login')