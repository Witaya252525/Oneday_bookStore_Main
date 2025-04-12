from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request,id):
    # greeting = "your ID : {000}".format(id)
    greeting = f"your ID is == {id}"
    return HttpResponse(greeting)


def article(request,year,slug):
    # greeting = "your ID : {000}".format(id)

    return HttpResponse(f"<h1>Witaya Chaison {year} {slug}</h1>")


def index(request):
    id ='001'
    name = 'Witaya'
    email ='witaya.chaison@gmail.com'
    
    activities = [ 'Football' , 'Running' ,'Badminton']


    # greeting = "your ID : {000}".format(id)
    return render(request, "index.html" ,{

    'id1' : id ,
    'name1' : name ,
    'email1' : email,
    'activities':   activities

    })
