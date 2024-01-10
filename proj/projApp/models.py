from django.db import models
from django.core import validators
# Create your models here.

class User(models.Model):
    f_name = models.CharField(max_length=64, default='')
    l_name = models.CharField(max_length=64, default='')
    age = models.IntegerField(default=18)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=32,default='')

    @staticmethod
    def hashPassword(password):

    @property
    def skills(self):
        skill_list = []

class Vacancy(models.Model):
    pass

