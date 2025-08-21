# LibraryProject

A Django project built as part of the **Advanced Features and Security** module.  
This project demonstrates permission management, authentication, and secure handling of user roles while managing a simple book library.

---

##  Project Structure
advanced_features_and_security/
│
├── LibraryProject/          # Main Django project folder
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── bookshelf/               # Core app for managing books
│   ├── migrations/
│   ├── templates/
│   │   └── bookshelf/
│   │       └── book_list.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
└── manage.py

---

## Features

- User authentication (login/logout)
- Permission-based access to views
- CRUD operations for `Book` models
- Secure routing and template rendering

---

## Prerequisites

- Python 3.8+
- Django 4.x
- SQLite (default) or PostgreSQL/MySQL (optional for production)
- Git (for version control)

---

## Installation

1. **Clone the repository**

   ```bash
   git clone <your-repo-url>
   cd advanced_features_and_security/LibraryProject

### Create and Activate a Virtual Environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

### Install Dependancies
pip install -r requirements.txt

### Run Migrations
python manage.py migrate

### Create Superuser
python manage.py createsuperuser

### Start the Development Server
python manage.py runserver

### Open Browser
Open your browser and visit:
http://127.0.0.1:8000/books/


## Permissions
The book_list view is protected by the view_book permission.
* Ensure your superuser or staff users have the bookshelf.view_book permission assigned.
* You can manage permissions via the Django admin interface: http://127.0.0.1:8000/admin/

## Testing
Run automated tests with : python manage.py test

## Deployment
For production:
* Use a WSGI/ASGI server like Gunicorn or Daphne
* Configure allowed hosts in settings.py
* Run database migrations and collect static files:

python manage.py migrate
python manage.py collectstatic