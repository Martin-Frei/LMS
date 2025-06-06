from django import forms
from alertSystem.models import alert

class alertForm(forms.ModelForm):
    class Meta:
        model= alert
        fields = ['alertTitle','alertText','alertType','alertType' ]
        
