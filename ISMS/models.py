from django.db import models

# Create your models here.


class Pessoa(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self) -> str:
        return self.name
