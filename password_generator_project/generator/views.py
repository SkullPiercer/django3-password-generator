from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxuz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXUZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_-=+'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    lenght = int(request.GET.get('lenght', 12))
    if int(request.GET.get('lenght')) > 14 or int(request.GET.get('lenght')) < 6:
        thepassword = 'Указанное кол-во символов недопустимо!'
        return render(request, 'generator/password.html', {'password':thepassword})
    thepassword = ''
    for x in range(lenght):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})

def description(request):
    return render(request, 'generator/description.html')
