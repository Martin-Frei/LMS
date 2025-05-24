# 📚 Library Management System (LMS)

A simple web-based Library Management System built with [Django](https://www.djangoproject.com/). This project helps manage books, users, borrowings, and alert notifications.

---

## 🔧 Project Overview

The LMS consists of multiple Django apps:

- `manageBooks` – Add or remove books
- `alertSystem` – Manage alerts (e.g., overdue notifications)
- `manageRentals` – Track and manage active and past rentals
- `manageRentTime` – Define and monitor rental durations
- `manageUser` – User management

---

## 📂 Project Structure

```text
LMS/
├── LMS/                   # Django project folder (settings, URLs, WSGI/ASGI)
│   └── urls.py            # Global URL configuration
├── manageBooks/           # Book management app
├── alertSystem/           # Alert system app
├── manageRentals/         # Rental tracking app
├── manageRentTime/        # Rental time management app
├── manageUser/            # User management app
├── templates/             # HTML templates (incl. base.html)
├── static/                # CSS, JavaScript, images
└── db.sqlite3             # SQLite database (local development)