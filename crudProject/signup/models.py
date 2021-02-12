from django.db import models

class SignupDetails(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    reenter_password = models.CharField(max_length=20)

    def __str__(self):
        return self.firstname



