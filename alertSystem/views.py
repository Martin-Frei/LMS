from django.shortcuts import render
from alertSystem.forms import alertForm
from alertSystem.models import alert

# Create your views here.



def manageAlerts(request):
    data = alert.objects.all()
    if request.method == 'POST':
        form = alertForm(request.POST)
        if form.is_valid():
            form.save()
    context ={'alerts': alertForm,
               'alertDB':data}
    return render(request,'manageAlertsLMS.html', context )


