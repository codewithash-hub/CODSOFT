# 📌 Contact Book Application

## 📖 Overview
A Contact Book application is a project designed to help users manage and organize their contacts. This web-based application allows users to add, update, delete, and view their contacts, making it easier to stay in touch with important people. The project uses Django to create a web-based interface and SQLite for data storage.

## 🎯 Features
* ✅ Add new contacts
* ✏️ Edit or update contact details
* 📌 View contact information
* 🗑️ Delete contacts
* 📋 Search contacts by name or phone number

## 🛠️ Technologies Used
* Python
* Django (Web Framework)
* SQLite (Database)
* Bootstrap (For UI styling)
* CRUD Operations

## 📌 Usage

### 1️⃣ Clone the Repository
* git clone https://github.com/codewithash-hub/CODSOFT.git
* cd CONTACT_BOOK

### 2️⃣ Create a Virtual Environment (Recommended)
* python -m venv venv

##### Activate it:
* venv\Scripts\activate (For Windows)
* source venv/bin/activate (For macOS/Linux)

### 3️⃣ Install Dependencies
* pip install -r requirements.txt

### 4️⃣ Run Migrations
* python manage.py makemigrations
* python manage.py migrate

### 5️⃣ Run the Development Server
* python manage.py runserver

This will display an output like:
* Starting development server at http://127.0.0.1:8000/

### 6️⃣ Access the Application
Once the server is running, open your browser and navigate to `http://127.0.0.1:8000/`. You will be able to add, view, update, delete, and search for contacts.

## 📝 Folder Structure
```plaintext
contact_book/
    ├── contact_book/
    │   ├── migrations/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── views.py
    │   └── urls.py
    ├── manage.py
    ├── requirements.txt
    └── templates/
        └── contacts/
            ├── contact_list.html
            ├── add_contact.html
            ├── edit_contact.html
