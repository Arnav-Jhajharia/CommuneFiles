from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import datetime
import uuid
# Create your models here.

# Table storing all the users.


class User(AbstractUser):
    person_id = models.UUIDField(
        primary_key=False,
        default=uuid.uuid4)
    date = models.DateField(default=datetime.date(2000, 1, 1), null=True)
    description = models.TextField(default='', max_length=169)
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='following', through='Follower')

    def serialize(self):
        return {
            "person_id": self.person_id,
            "number": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username,
            "description": self.description,
            "email": self.email,
        }


# Table for all the followers and following with extra fields (space for extra fields)


class Follower(models.Model):
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='to_person', blank=True, null=True)
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='from_person', blank=True, null=True)
    when_followed = models.DateTimeField(blank=True, null=True)
