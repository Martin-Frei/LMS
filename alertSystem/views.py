from django.shortcuts import render

# Create your views here.



def manageAlerts(request):
    context ={}
    return render(request,'manageAlertsLMS.html', context )