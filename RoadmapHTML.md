    base.html:

    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>

    <body>
    </head>
        <header>
        <h1>{% block header_title %}Meine Hauptseite{% endblock %}</h1>

        {% block navbar %}
        <nav>
            
            <a href="{% url 'URLName1' %}">URLName2</a>
            <a href="{% url 'URLName1' %}">URLName3</a>
            <a href="{% url 'URLName1' %}">URLName4/a>
            <a href="{% url 'URLName1' %}">URLName5<a>
        </nav>
        {% endblock %}
    </header>

    <div class="sidebar">
        {% block side %}
        <p>Default Sidebar Content (z.B. Login-Info oder Links)</p>
        {% endblock %}
    </div>

    <main>
        {% block content %}
        <p>Default Main Content</p>
        {% endblock %}
    </main>

    <footer>
        <p>Mein Footer</p>
        <script src="{% static 'js/script.js' %}"></script>
    </footer>

    </body>
    </html>


    {% extends 'base.html' %}

    {% block header_title %}
    Spezielle Seite
    {% endblock %}

    {% block navbar %}
    <nav>
        <a href="{% url 'URLName1' %}">Start</a>
        <a href="{% url 'URLName2' %}">URLName2</a>
        <a href="{% url 'URLName3' %}">URLName3</a>
        <a href="{% url 'URLName4' %}">URLName4/a>
        <a href="{% url 'URLName5' %}">URLName5<a>
    </nav>
    {% endblock %}

    {% block title %}Spezielle Seite – Mein Projekt{% endblock %}

    {% block side %}
    <p>Benutzerstatus, Benachrichtigungen, etc.</p>
    {% endblock %}

    {% block content %}
    <h2>Willkommen auf der speziellen Seite</h2>
    <p>Hier steht dein spezieller Inhalt.</p>
    {% endblock %}
