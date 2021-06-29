from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from account.models import User_info
from opinion.models import Suggestion, Selection, Group_info, Membership, Response

# Create your views here.
def mainpage_view(request):
  # authorize_action(request)
  session_existence = authorization(request)
  if not session_existence:
    return redirect('login')
  group_list = get_group_list(request)
  return render(request, 'mainpage.html', {"group_list": group_list})


def grouppage_view(request, group_seq):
  # authorize_action(request)
  session_existence = authorization(request)
  request.session['group_seq'] = group_seq
  if not session_existence:
    return redirect('login')
  group_suggestion = get_group_suggestion(request)
  user_suggestion = get_user_suggestion(request)
  data = {}
  data['group_suggestion'] = group_suggestion
  data['user_suggestion'] = user_suggestion
  data['is_g_answered'] = []
  data['is_u_answered'] = []
  data['is_g_all_answered'] = []
  data['is_u_all_answered'] = []
  
  for suggestion in group_suggestion:
    if is_answered(request, suggestion.id):
      data['is_g_answered'].append(suggestion.id)
  for suggestion in user_suggestion:
    if is_answered(request, suggestion.id):
      data['is_u_answered'].append(suggestion.id)
  return render(request, 'grouppage.html', data)


def is_answered(request, suggestion_seq):
  user_email = request.session['user_email']
  user_seq = User_info.objects.get(user_email=user_email).user_seq
  try:
    Response.objects.get(writer_id=user_seq, suggestion_id=suggestion_seq)
  except:
    return False
  return True


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


def decision_view(request, suggestion_seq):
  # authorize_action(request)
  session_existence = authorization(request)
  if not session_existence:
    return redirect('login')
  name = get_session_name(request)
  suggestion = Suggestion.objects.get(id=suggestion_seq)
  selection_qs = Selection.objects.filter(suggestion_id=suggestion_seq)
  options = []
  for ele in selection_qs:
    options.append(ele.selection_content)
  request.session['suggestion'] = suggestion_seq
  return render(request, 'decision.html', {'name': name, 'suggestion': suggestion, 'options': selection_qs})


def decision_preserve(request):
  dataset = request.GET
  print("---Choice:", dataset.get('choice'))
  request.session['selection'] = dataset['choice']
  return HttpResponse('True')


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
  name = get_session_name(request)
  session_existence = authorization(request)
  if not session_existence:
    return redirect('login')
  return render(request, 'decision_reason.html', {'name': name})


def decision_submit(request):
  # authorize_action(request)
  session_existence = authorization(request)
  if not session_existence:
    return redirect('login')
  print("---GET DATA: ", request.GET)
  content = request.GET['reason']
  selection_seq_id = request.session['selection']
  suggestion_id = request.session['suggestion']
  writer_id = User_info.objects.get(user_email=get_session_email(request)).user_seq
  response = Response()
  response.content = content
  response.selection_seq_id = selection_seq_id
  response.suggestion_id = suggestion_id
  response.writer_id = writer_id
  response.save()
  return HttpResponse('True')


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


def create_group(request):
  session_existence = authorization(request)
  if not session_existence:
    return HttpResponse('False')
  email = get_session_email(request)
  dataset = request.GET
  name = dataset.get('name')
  group = Group_info()
  group.name = name
  group.owner = User_info.objects.get(user_email = email)
  group.save()
  
  membership = Membership()
  membership.group = group
  membership.user = User_info.objects.get(user_email = email)
  membership.auth = "S"
  membership.save()
  return HttpResponse('True')


def create_suggestion(request):
  session_existence = authorization(request)
  if not session_existence:
    return HttpResponse('False')
  dataset = request.GET
  title = dataset.get('title')
  options = []
  index = 0
  while True:
    selection_key = 'selection' + str(index)
    if selection_key in dataset:
      options.append(dataset[selection_key])
      index += 1
    else:
      break
  
  # Create Suggestion
  suggestion = Suggestion()
  suggestion.group_sequence = Group_info.objects.get(group_seq = request.session['group_seq'])
  suggestion.topic = title
  suggestion.other_selection = True
  suggestion.no_selection = True
  suggestion.owner_seq = User_info.objects.get(user_email = get_session_email(request)).user_seq
  suggestion.save()
  
  # Create option matched to upper created suggestion
  for index in range(0, len(options)):
    selection = Selection()
    selection.suggestion = suggestion
    selection.selection_content = options[index]
    selection.save()
  return HttpResponse('True')
  
  
def authorization(request):
  return ('user_email' in request.session)


def get_session_email(request):
  if authorization(request):
    print("---SESS EMAIL:",request.session['user_email']) 
    return request.session['user_email']


def get_session_name(request):
  if authorization(request):
    print("SESS EMAIL:",request.session['user_email'])
    user = User_info.objects.get(user_email = request.session['user_email'])
    return user.user_name
  

def authorize_action(request):
  session_existence = authorization(request)
  print("sess", session_existence)
  if not session_existence:
    return redirect('login')
  
  
def get_group_list(request):
  user_email = get_session_email(request)
  user = User_info.objects.get(user_email = user_email)
  membership_qs = Membership.objects.filter(user = user)
  group_list = []
  for ele in membership_qs:
    group_list.append(ele.group)
  return group_list


def get_group_suggestion(request):
  group_seq = request.session['group_seq']
  user_email = get_session_email(request)
  user = User_info.objects.get(user_email = user_email)
  suggestion_list = Suggestion.objects.filter(group_sequence=group_seq).exclude(owner_seq=user.user_seq)
  return suggestion_list


def get_user_suggestion(request):
  group_seq = request.session['group_seq']
  user_email = get_session_email(request)
  user = User_info.objects.get(user_email = user_email)
  suggestion_list = Suggestion.objects.filter(group_sequence=group_seq, owner_seq=user.user_seq)
  return suggestion_list