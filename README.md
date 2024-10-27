# Plateforme E-Learning

Welcome to **Plateforme E-Learning**, a comprehensive learning management system built with Django. This platform aims to support online learning through accessible tools and resources.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Step 1: Clone the Repository](#1-clone-the-repository)
  - [Step 2: Set Up a Virtual Environment](#2-set-up-a-virtual-environment)
  - [Step 3: Install Dependencies](#3-install-dependencies)
  - [Step 4: Configure Environment Variables](#4-configure-environment-variables)
  - [Step 5: Apply Database Migrations](#5-apply-database-migrations)
  - [Step 6: Create a Superuser](#6-create-a-superuser)
  - [Step 7: Run the Server](#7-run-the-server)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Features

- **User Authentication:** Secure login and registration system.
- **Admin Panel:** Management of users, courses, and resources through Django’s admin interface.
- **Course Management:** Add, edit, and delete courses with easy-to-use interfaces.
- **Interactive Content:** Support for videos, quizzes, and additional resources.
- **Responsive Design:** Accessible across devices for optimal user experience.

## Prerequisites

Ensure the following are installed:

- **Python** 3.10 or higher
- **pip** for package management
- **virtualenv** for creating isolated environments

## Installation

### 1. Clone the Repository

Start by cloning the repository from GitHub:

```bash
git clone https://github.com/HamzaAitahmed/Plateforme_E_Learning.git
cd Plateforme_E_Learning
```

### 2. Set Up a Virtual Environment

Create and activate a virtual environment to manage dependencies:

- **On Linux**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

- **On Windows**:
  ```bash
  pip install virtualenv
  virtualenv --python python venv
  .\venv\bin\activate
  ```

### 3. Install Dependencies

Install required packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

Run migrations to initialize the database schema:

```bash
python manage.py migrate
```

### 5. Create a Superuser

Set up an admin account for accessing Django’s admin interface:

```bash
python manage.py createsuperuser
```

### 6. Run the Server

Launch the server locally:

```bash
python manage.py runserver
```

The application should now be accessible at `http://127.0.0.1:8000/`.

**Email**: hamza@gmail.com
**PassWord**: 123

## Project Structure

```plaintext
Plateforme_E_Learning/
│
├── E_Learning/  # Main Django project directory
│   ├── __init__.py         # Marks the directory as a Python package
│   ├── settings.py         # Project settings, including installed apps and middleware
│   ├── urls.py             # URL routing for the project
│   ├── wsgi.py             # WSGI configuration for deployment
│   └── asgi.py             # ASGI configuration for asynchronous support
│
├── <app_name>/             # Django app containing specific features of the platform
│   ├── migrations/         # Database migration files for the app
│   ├── __init__.py         # Marks the directory as a Python package
│   ├── admin.py            # Admin panel configurations
│   ├── apps.py             # Application configuration
│   ├── models.py           # Database models for the app
│   ├── tests.py            # Test cases for the app
│   ├── url.py              # URL routing specific to the app
│   └── views.py            # Application logic and routing
|
│── static/                 # Static assets (CSS, JavaScript, images) for the app
│── templates/              # HTML templates for the app
|
├── db.sqlite3              # SQLite database file (created after running migrations)
├── manage.py               # Django's main management script
├── requirements.txt        # Project dependencies
|
└── other_directories/      # Additional directories as needed
```

## Usage

- **Admin Access**: Log into the admin panel at `/admin` using the superuser credentials created earlier.
- **Adding Content**: Use the admin panel to manage courses, users, and other learning resources.
- **Exploring as a User**: Access the platform’s main features by creating a regular user account and logging in.

## Troubleshooting

- **Common Issues**:
  - **Dependency Conflicts**: Ensure all packages in `requirements.txt` are installed in the virtual environment.
