from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Room, Message

# Create your views here.


@login_required
def rooms(request):
    try:
        rooms = Room.objects.filter(user=request.user)
        print(rooms)
    except:
        rooms: Room.objects.get(name="Hello")
    return render(request, 'chat/room/chatrooms.html', {'rooms': rooms})


@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'chat/room/chatroom.html', {'room': room, 'messages': messages})
