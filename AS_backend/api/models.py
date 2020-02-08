from django.db import models
import jsonfield



class Item(models.Model):
    description = models.CharField(max_length=500)
    price = models.CharField(max_length=20)
    link = models.CharField(max_length=250)
    category = models.CharField(max_length=100)
    site_name = models.CharField(max_length=50)
    image = models.CharField(max_length=250)
    specs = jsonfield.JSONField()
    unit = models.CharField(max_length=10)
    time = models.CharField(max_length=20)


class User(models.Model):
    name = models.CharField(max_length=50)
    # TODO find a way to store an encrypted password



class Assembly(models.Model):
    name = models.CharField(max_length=50)
    items = models.ManyToManyField(Item)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


