import django.contrib.admin
from django.contrib import admin
from projApp.models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Vacancy)
admin.site.register(Skills)

admin.site.register(UserSkills)
admin.site.register(VacancySkills)
