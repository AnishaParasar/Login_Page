from django.db import models

# Create your models here.
class Item(models.Model):
    user = models.TextField(max_length=191)
    fname = models.TextField(max_length=20, null=True)
    mname = models.TextField(max_length=20, null=True)
    lname = models.TextField(max_length=20, null=True)
    email = models.TextField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
