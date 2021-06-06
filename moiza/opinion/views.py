from django.shortcuts import render

def mainpage_view(request):
  return render(request, 'mainpage.html')

def suggestion_view(request):
  return render(request, 'suggestion.html')