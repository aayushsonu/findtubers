from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    user = models.ManyToManyField(User)
    # user = models.ManyToManyField(
    #     User, related_name="roomuser", on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    # client_name = models.ForeignKey(
    #     User, related_name='client_name', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Message(models.Model):
    room = models.ForeignKey(
        Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)
