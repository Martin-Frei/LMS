Django-Projekt Setup & Workflow
1️⃣ Django-Projekt erstellen
django-admin startproject projektname

2️⃣ Virtuelle Umgebung starten
C:\Users\Martin\VSCode\venv\Scripts\activate

3️⃣ App erstellen
python manage.py startapp appname

4️⃣ App in settings.py registrieren
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    # ... andere Standard-Apps
    'appname',  # ← Hier jede deiner Apps eintragen
]

5️⃣ BASE_DIR in settings.py kontrollieren / setzen
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

6️⃣ Funktionen in views.py der jeweiligen App schreiben
from django.shortcuts import render

# Beispiel für eine einfache View-Funktion
def funktionname(request):
    # Logik hinzufügen
    pass

# Beispiel für eine View mit Template-Rendering
def funktionname(request):
    context = {}
    return render(request, 'templatename.html', context)

7️⃣ URLs in urls.py registrieren
from appname import views as appname_views
from django.urls import path # Wichtig: path importieren, falls noch nicht geschehen

urlpatterns = [
    path('route/', appname_views.funktionname, name='url_name'),
]
# route: Pfad in der URL, z.B. http://127.0.0.1:8008/route/
# view: Funktion in views.py, die aufgerufen wird, z.B. appname_views.funktionname
# name: URL-Name zum Verweisen im Template, z.B. {% url 'url_name' %}

8️⃣ Statische Dateien organisieren
Ordnerstruktur:

static/
├── css/
├── fonts/
├── img/
└── js/

In settings.py statische Dateien registrieren:

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

9️⃣ Templates erstellen
Ordner templates/ im Projektverzeichnis anlegen

Grundtemplate (base.html) erstellen

Weitere Templates für einzelne Views anlegen

🔟 Virtuelle Umgebung aktivieren (zur Erinnerung)
C:\Users\Martin\VSCode\venv\Scripts\activate

1️⃣1️⃣ Entwicklungsserver starten
python manage.py runserver 8008


django-admin startproject projektname

venv starten 
C:\Users\Martin\VSCode\venv\Scripts  activate


python manage.py startapp appname



App in Settings.py registrieren
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    # ... andere Standard-Apps
    'appname',                  ← Hier jede deiner App eintragen
]

kontrollieren ob BASE_DIR gesetzt ist 
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


Funktionen in Views.py in der jeweilige appname schreiben 
    def funktionname(request):
        # Logik, um funktion hinzuzufügen
        pass

    Standart Funktionen
    def funktionname(request):
        context ={}
        return render(request, 'templatename.html', context)



Url.py wie folgt 
    from appname import views as appname 
    (oder app_views oder ähnliches)

    path(route, view, name= URLName (irgendetwas,aber passend))
    route = http://127.0.0.1:8008/(name)
    view = appname.funktionname (aus der Views)
    name =  name der Url, um auf diesen Pfad zu verweisen 
    {% url 'URLNmae' %}

Ordner Static erstellen
    Unterordner mit CSS FONT IMG JS 
    Static registrieren in Settings.py:

    STATIC_URL = '/static/'
    STATICFILES_DIRS = [BASE_DIR / "static"]
    STATIC_ROOT = BASE_DIR / "staticfiles"


Template.html erstellen 
    Ordner template anlegen in der obersten Struktur 
    Grundtemplate erstellen 
    und die anderen contenttemplates ()
    base.html:
    URLName1
    URLName2
    URLName3
    URLName4
    URLName5

Jedes Template bekommt eine Funktion in der jeweiligen appname/views
und wird in der URL.py eingetragen



  

venv starten 
C:\Users\Martin\VSCode\venv\Scripts  activate

Server starten
C:\Users\Martin\VSCode\Phyton\Django/projektname   python manage.py runserver 8008
