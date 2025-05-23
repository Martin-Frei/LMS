from django.shortcuts import render

# Create your views here.

def manageRentals(request):
    context ={}
    return render(request,'manageRentalLMS.html', context )