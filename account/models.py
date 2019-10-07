from django.db import models

# Create your models here.
class User(models.Model):
    id = models.EmailField(verbose_name="user_email",primary_key=True,unique=True, blank=False)
    password =models.CharField(max_length=50)