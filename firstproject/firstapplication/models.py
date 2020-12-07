from django.db import models

class First(models.Model):
    name = models.CharField(max_length=50)
    contact = models.IntegerField()
    address = models.TextField()

def __str__(self):
    return self.name


