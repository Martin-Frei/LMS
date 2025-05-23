"""
URL configuration for LMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from manageBooks import views as book_views
from alertSystem import views as alert_views
from manageRentals import views as rental_views
from manageRentTime import views as time_views
from manageUser import views as user_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', book_views.index, name='main'),

    path('addBook', book_views.addBook, name='add_book'),
    path('removeBook', book_views.removeBook, name='remove_book'),

    path('manageBooks', book_views.manageBook, name='manage_books'),
    path('manageRentals', rental_views.manageRentals, name='manage_rentals'),
    path('manageRentTime', time_views.manageRentTime, name='manage_time'),
    path('manageAlerts', alert_views.manageAlerts, name='alerts'),
    path('manageUser', user_views.manageUser, name='manage_user'),
]
