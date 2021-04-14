from django.db import models


class Personal(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.CharField(max_length=2)
    Skills = models.CharField(max_length=200)

class Color(models.Model):
    clr = models.CharField(max_length=100)


# Create your models here.
