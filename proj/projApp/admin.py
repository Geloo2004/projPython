import django.contrib.admin
from django.contrib import admin
from projApp.models import *

# Register your models here.

django.contrib.admin.register(User)
django.contrib.admin.register(Vacancy)
