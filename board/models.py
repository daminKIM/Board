from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()   
    create_date=models.DateTimeField(auto_now_add=True)
    modify_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]


class Comment(models.Model):
    user = models.ForeignKey('account.User',on_delete=models.CASCADE, related_name="comment_user")
    body = models.TextField(primary_key=True)
    create_date=models.DateTimeField(auto_now_add=True)
    modify_date=models.DateTimeField(auto_now=True)

