from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name + " " + self.color