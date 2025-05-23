from django.shortcuts import render

# Create your views here.


def manageRentTime(request):
    context ={}
    return render(request,'manageRentalLMS.html', context )