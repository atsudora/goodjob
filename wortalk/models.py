from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# 投稿するモデル
class Post(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  #アカウント削除に付随して投稿も削除
    date_posted = models.DateField(default=timezone.now)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.content[:25]
    