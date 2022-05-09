from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('chatroom/', include('chat.chatroom.urls'))
]
