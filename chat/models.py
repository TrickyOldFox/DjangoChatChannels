from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    room_name = models.CharField(max_length = 20)

    def __str__(self):
        return self.author.username

    def last_10_messages(room_name):
        try:
            messages = Message.objects.filter(room_name = room_name).order_by('-timestamp')[:10]
            return reversed(messages)
        except:
            return None

    def active_conversations(user):
        room_names = Message.objects.filter(author=user).values_list('room_name', flat=True).distinct()
        messages=[]
        for i in room_names:
            try:
                message = Message.objects.filter(room_name = i).order_by('-timestamp')[0]
                messages.append(message)
            except: pass
        return messages
