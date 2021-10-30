from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import datetime
import uuid
# Create your models here.

# Table storing all the users.

GENRES = [
    [0, "General"],
    [1, "Education"],
    [2, "Pop Culture"],
    [3, "Sports"],
    [4, "Science and Tech"]
]


class User(AbstractUser):
    post = models.ManyToManyField(Post, blank=True, null=True)

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


class Post(models.model):
    text = models.TextField(max_length=256)
    relevancy = models.IntegerField(max_length=2, null=True, default=0)
    time_posted = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, null=True, related_name='user_likes')
    genre = models.CharField(max_length=1, default=1)


class Main_Post(Post):
    def get_relevancy(self):
        x = datetime.datetime.now()
        timeElapsedSincePost = x.minutes - self.time_posted.minutes
        relevancy = 100
        relevancy = relevancy - timeElapsedSincePost
        relevancy = relevancy + 8 * self.likes
        if self.text in GENRES[self.genre][1]:
            relevancy += 10
        else:
            relevancy -= 10
        return relevancy
