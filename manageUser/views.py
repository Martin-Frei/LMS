from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def manageUser(request):
    context ={}
    return render(request,'manageUserLMS.html', context )