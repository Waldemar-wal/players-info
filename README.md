# Players-info

A Django-based project for managing RPG game elements. Supports full CRUD (Create, Read, Update, Delete) 
operations for the following entities:

- Players
- Races
- Equipment
- Equipment Types

## 🚀 Features

- CRUD interface for all entities
- Django admin panel
- REST API (optional, if using DRF)
- Simple and extensible architecture (e.g., add classes, skills, etc.)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/Waldemar-wal/players-info
````
2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Apply migrations:
```bash
python manage.py migrate
```
5. Create a superuser (to access the admin panel):
```bash
python manage.py createsuperuser
```
6. Run the development server:
```bash
python manage.py runserver
```

🔒 Admin Panel

Once the server is running, go to:
http://127.0.0.1:8000/admin/

Log in with the superuser credentials to manage all entities through the Django admin interface.

🧩 Possible Extensions

   - Character classes

   - Skills / abilities

   - Combat system

   - User authentication and profiles


