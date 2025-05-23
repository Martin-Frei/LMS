from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def addBook(request):
    return HttpResponse(" First Comment")


def removeBook(request):
    return HttpResponse("Book to remove")


def manageBook(request):
    context ={}
    return render(request,'manageBookLMS.html', context )

def index(request):
    context ={}
    return render(request,'mainLMS.html', context )