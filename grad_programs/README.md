# Graduate Programs Django Application

This is a Python Django application for managing and displaying graduate programs. It allows users to search and filter programs based on various criteria.

## Prerequisites

Before you begin, ensure you have the following installed on your Windows 10 machine:

- [Python](https://www.python.org/downloads/) (version 3.8 or higher)
- [pip](https://pip.pypa.io/en/stable/) (Python package installer, usually included with Python)


## Navigate to the Project Directory

```cd grad_programs```


## Create a Virtual Environment
```python -m venv venv```
```venv\Scripts\activate```
```source venv/bin/activate```

## Install Required Packages

```pip install -r requirements.txt```

## Apply Migrations

```python manage.py makemigrations```
```python manage.py migrate``

## Load data into database

```python manage.py loaddata data.json```

## Start the Django development server

```python manage.py runserver```

## Open your web browser and navigate to:

```http://127.0.0.1:8000/```
