from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    followers = models.ManyToManyField("self", related_name="followers")
    follow = models.ManyToManyField("self", related_name="follows")

    def no_of_followers(self):
        return self.followers.count()
    
    def no_of_follows(self):
        return self.follow.count()
    

class Create(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner",null=False)
    createdOn = models.DateTimeField(auto_now_add=True, auto_now=False)
    modifiedOn = models.DateTimeField(auto_now=True)
    post = models.TextField()
    like = models.ManyToManyField(User, related_name='like')

    def number_of_likes(self):
        return self.like.count()
    




