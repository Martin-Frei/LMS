from django import forms
from manageUser.models import user

class UserForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ['userType', 'userGender', 'userFirstName', 'userSecondName', 'userStreetName','userHouseNumber','userZipCode', 'UserCityName', 'userEmail', 'userPhone', 'userBirthday']
 