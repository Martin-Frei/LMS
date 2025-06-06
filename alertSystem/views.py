from django.shortcuts import render
from alertSystem.forms import alertForm

# Create your views here.



def manageAlerts(request):
    if request.method == 'POST':
        form = alertForm(request.POST)
        if form.is_valid():
            form.save()
    context ={'alerts': alertForm}
    return render(request,'manageAlertsLMS.html', context )


