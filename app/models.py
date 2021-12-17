from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=100, unique=True)

    # class Meta:
    #     ordering = ('name',)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=255)
    std_id = models.CharField(max_length=7)
    email = models.EmailField(max_length=20, unique=True)

    class Meta:
        ordering = ('std_id',)

    def __str__(self):
        return self.name
