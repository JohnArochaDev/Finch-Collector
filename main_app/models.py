from django.db import models

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    bird = models.BooleanField(default=False)
    age = models.IntegerField()
    def __str__(self):
        return self.name

