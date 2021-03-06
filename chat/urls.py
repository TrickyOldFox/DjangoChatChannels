from django.urls import path, re_path
from .views import index, room, chat_lobby


app_name = 'chat'

urlpatterns = [
    path('', chat_lobby, name='chat_lobby'),
    path('lobby/', chat_lobby, name='chat_lobby'),
    re_path(r'^(?P<room_name>[^/]+)/$', room, name='room'),
]
