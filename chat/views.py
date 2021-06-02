from django.shortcuts import render
from django.http import JsonResponse
from .models import Room
import json
# List format - [["username","message"],["username","message"]]
# Create your views here.
def lobby(request,lobby,username):
    if len(Room.objects.filter(Name=lobby)) == 0:
        chat = json.dumps([])
        NewRoom = Room(Name = lobby,Chat=chat)
        NewRoom.save()
        context = {"New":True,"LobbyName":lobby}
        return render(request,"room.html",context)
    room = Room.objects.filter(Name=lobby)[0]
    chatlist = room.Chat
    LobbyName = room.Name
    context = {"ChatList":chatlist,"LobbyName":LobbyName,"username":username,"New":False}
    return render(request,"room.html",context)

def Newmssg(request):
    NMssg = request.POST.get("mssg")
    User = request.POST.get("user")
    RoomName = request.POST.get("room")
    room = Room.objects.filter(Name=RoomName)[0]
    chat = json.loads(room.Chat)
    chat.append([User,NMssg])
    room.Chat = json.dumps(chat)
    room.save()
    return JsonResponse({"ChatList":chat})

def Update(request):
    CurrentStatus = request.POST.get("currentStatus")
    RoomName = request.POST.get("room")
    room = Room.objects.filter(Name=RoomName)[0]
    Chat = json.loads(room.Chat)
    while True:
        if Chat != CurrentStatus:
            return JsonResponse({"chatlst":Chat})