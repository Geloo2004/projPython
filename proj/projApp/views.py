from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from models import *
import models
# Create your views here.

@csrf_exempt
def main(request):
    return render(request,'main.html')

@csrf_exempt
def register(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    if not (email == None or password == None):
        try:
            User.objects.create(email=email,password=password)
            return render(request,'register.html', context={'message': 'success'})
        except Exception as e:
            return render(request,'register.html', context={'message': e})
    else:
        print('nonetype')
        return render(request,'register.html', context={'message': 'noneType'})
