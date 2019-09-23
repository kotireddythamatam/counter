from django.db import models

# Create your models here.
class Login(models.Model):
    Username = models.CharField(max_length=64,blank=True,null=True)
    Password = models.CharField(max_length=64,blank=True,null=True)
    Counter = models.PositiveIntegerField()
    datetime = models.DateTimeField(auto_now_add=True)
