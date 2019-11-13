from django.db import models

# Create your models here.
class Detail(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=16)
    fullname = models.CharField(max_length=255)
    address = models.TextField()
    registered = models.DateTimeField(auto_now_add=True)
    cash = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    level = models.IntegerField(default=0)

class Portfolio(models.Model):
    user_id = models.ForeignKey(Detail, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    number = models.IntegerField()