from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def main_view(request):
    return HttpResponse("This is the main page for Phone Radar website")


def index_view(request):
    context = {"greetings": "Welcome to Week 4 - The Views!"}
    return render(request, "main/index.html", context)
