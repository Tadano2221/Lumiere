from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'eduweb/index.html')

def chat(request):
    return render(request, 'eduweb/chat.html')

def room(request, room_name):
    return render(request, "eduweb/room.html", {"room_name": room_name})