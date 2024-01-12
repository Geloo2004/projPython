from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from projApp.models import *

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
            print('success')
            return render(request,'register.html', context={'message': 'success'})
        except Exception as e:
            print('no success')
            return render(request,'register.html', context={'message': e})
    else:
        print('nonetype')
        return render(request,'register.html', context={'message': 'noneType'})
