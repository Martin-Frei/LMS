 projektname/
│
├── manage.py
│
│── projektname/                ← Hier liegt das eigentliche Projekt-Package
│    ├── __init__.py
│    ├── asgi.py
│    ├── settings.py
│    ├── urls.py
│    └── wsgi.py  
│   
│── appname/                     ← Deine App
│    ├── __init__.py             ← Macht den Ordner zu einem Python-Package
│    ├── admin.py                ← Hier registrierst du Models für die Admin-Oberfläche
│    ├── apps.py                 ← Konfigurationsdatei der App
│    ├── models.py               ← Hier definierst du deine Datenbankmodelle
│    ├── tests.py                ← Hier schreibst du Unittests für die App
│    ├── views.py                ← Hier definierst du deine Views/Controller-Logik
│    └── migrations/ 
│
├── static/                      ← optional, für projektweite statische Dateien
│   ├── css/
│   ├── js/
│   ├── img/
│   └── fonts/ 
│
├── templates/                   ← Templates Ordner global
│   ├── base.html
│   ├── URLName1
│   ├── URLName2
│   ├── URLName3
│   ├── URLName4
│   └── URLName5