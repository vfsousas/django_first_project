from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    my_dict = {"insert_me": "Hello  I am from the views.py in MyFirstApp"}
    return render(request, 'MyFirstApp/index.html', context=my_dict)

# Create your views here.
