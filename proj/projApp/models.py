from django.db import models
from django.core import validators
import datetime
import hashlib
# Create your models here.

class User(models.Model):
    f_name = models.CharField(max_length=64, default='')
    l_name = models.CharField(max_length=64, default='')
    age = models.IntegerField(default=18)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=32,default='')

    def verifyPassword(self, input_password):
        input_password_hashed = hashlib.md5(input_password.encode())
        return input_password_hashed == self.password

    @staticmethod
    def hashPassword(password):
        return hashlib.md5(password.encode())
    @staticmethod
    def verifyAge(age):
        return age >= 18 or age <= 100

class Vacancy(models.Model):
    pass

class UserSkills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    skills = []



