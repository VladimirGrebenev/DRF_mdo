from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4


# Create your models here.
class Property(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, verbose_name='id')
    key = models.CharField(max_length=128)
    value = models.CharField(max_length=500)

    def __str__(self):
        return self.value


class Entity(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, verbose_name='id')
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField(null=True, blank=True)
    properties = models.ManyToManyField(Property)

