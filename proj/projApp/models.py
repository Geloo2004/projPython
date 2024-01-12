from django.db import models
from django.core import validators
import datetime
import hashlib
# Create your models here.

class User(models.Model):
    f_name = models.CharField(max_length=64, default='')
    l_name = models.CharField(max_length=64, default='')
    age = models.IntegerField(default=18)
    email = models.EmailField(unique=True, default='')
    password = models.CharField(max_length=32,default='')

    @property
    def skills(self):
        skills_list = []
        for vacancy in self.userskill_set.all():
            skills_list.append(vacancy.skill.name)
        return skills_list

    def verifyPassword(self, password):
        h2 = hashlib.md5()
        h2.update(password.encode())
        b = h2.hexdigest()
        return self.password == b

    @staticmethod
    def hashPassword(password):
        h1 = hashlib.md5()
        h1.update(password.encode())
        a = h1.hexdigest()
        return a

    @staticmethod
    def verifyAge(age):
        return age >= 18 or age <= 100

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Vacancy(models.Model):
    name = models.TextField(default='')
    salary = models.IntegerField(default=0)
    area_name = models.TextField(default='')
    created_at = models.DateTimeField(default=datetime.datetime.now())

    @property
    def skills(self):
        skills_list = []
        for vacancy in self.vacancyskill_set.all():
            skills_list.append(vacancy.skill.name)
        return skills_list

    class Meta:
        verbose_name = 'vacancy'
        verbose_name_plural = 'vacancies'

class Skills(models.Model):
    name = models.TextField(default='')

    class Meta:
        verbose_name = 'skill'
        verbose_name_plural = 'skills'

class UserSkills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    skills = models.ForeignKey(Skills, on_delete=models.CASCADE, default='')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'skills'], name='cnstr_us')
        ]
        verbose_name = 'user_skills'
        verbose_name_plural = 'user_skills'

class VacancySkills(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, default='')
    skills = models.ForeignKey(Skills, on_delete=models.CASCADE, default='')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['vacancy', 'skills'], name='cnstr_vs')
        ]
        verbose_name = 'vacancy_skills'
        verbose_name_plural = 'vacancy_skills'