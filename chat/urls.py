from django.urls import path
from . import views
urlpatterns = [
    path("<str:lobby>/<str:username>",views.lobby,name="Lobby"),
    path("newmssg",views.Newmssg,name="New Message"),
    path("update",views.Update,name="Update"),
]