from django.shortcuts import render
import opinion.views

# Create your views here.

def mainpage_view(request):
    return render(request, 'mainpage.html')

def grouppage_view(request):
    return render(request, 'grouppage.html')

def listpage_view(request):
    return render(request, 'listpage.html')