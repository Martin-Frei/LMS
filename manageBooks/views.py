from django.shortcuts import render
from django.http import HttpResponse
from manageBooks.forms import manageBook
from manageBooks.models import bookRecord



# Create your views here.
# def addBook(request):
#     return HttpResponse(" First Comment")


# def removeBook(request):
#     return HttpResponse("Book to remove")


# def manageBook2(request):
#     bookname= ['How to built Django','How to biuld Webpages',' How to learn Python','How to learn Java Script']
#     ISBN= [1234567890,1212121212, 3434343434, 5656565656]
    
#     context ={'bookDetail': zip(bookname, ISBN)}
    
#     return render(request,'manageBookLMS.html', context )

def index(request):
    if request.method =="POST":
        fill_form = manageBook(request.POST)
        if fill_form.is_valid():
            fill_form.save()
    
    data = bookRecord.objects.all()
    context ={'manage_Book': manageBook,
              'bookDB': data}
    return render(request,'manageBookLMS.html', context )

