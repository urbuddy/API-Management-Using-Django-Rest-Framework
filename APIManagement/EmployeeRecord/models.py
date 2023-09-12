from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    salary = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.pk}--{self.name}"
