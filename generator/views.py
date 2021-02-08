from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'home.html', )

def about(request):
    return render(request, 'about.html', )

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    uppercharacters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    specialcharacters = list('.,+-*/?%£$')
    if request.GET.get('uppercase'):
        characters.extend(uppercharacters)
    if request.GET.get('special'):
        characters += specialcharacters
    length = int(request.GET.get('length',10))
    thepassword = ''
    for i in range(length):
        thepassword += random.choice(characters)
    return render(request, 'password.html',{'password':thepassword})
