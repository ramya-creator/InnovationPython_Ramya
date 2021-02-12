from django.db import models

class newblog(models.Model):
    EmpName = models.CharField(max_length=20)
    Domain = models.CharField(max_length=20)

    def __str__(self):
        return self.EmpName

