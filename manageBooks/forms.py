from django import forms
from manageBooks.models import bookRecord

class manageBook(forms.ModelForm):
    class Meta:
        model = bookRecord
        fields = ['bookName','bookAuthor','bookYear','isbn']
        