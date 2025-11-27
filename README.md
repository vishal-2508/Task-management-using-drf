
# Task Management using DRF

A task management application built using Django and Django Rest Framework (DRF). This application allows users to create, update, retrieve, and delete tasks. It also supports user authentication and authorization to manage access.

## Features

* User Authentication: Users can register and login their accounts. <br>
* Task CRUD Operations: Users can create, read, update, and delete tasks. <br>
* Task Filtering: Users can filter tasks based on their completion status and priority. <br>
* API Endpoints: Provides RESTful API for task management.

## Technologies Used

* Django: Python web framework used for backend development. <br>
* Django Rest Framework (DRF): Toolkit for building Web APIs in Django. <br>
* SQLite: Database for storing task data (depending on configuration). <br>
* JWT: JSON Web Tokens for user authentication.

## Installation and Setup

To get this project up and running locally, follow these steps:

1. Clone the repository <br>
git clone https://github.com/vishal-2508/Task-management-using-drf.git <br>
cd Task-management-using-drf

2. Set up a virtual environment (optional but recommended) <br>
* If you don't have virtualenv installed, install it using: <br>
pip install virtualenv <br>
* Create and activate the virtual environment: <br>
virtualenv venv <br>
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

3. Install dependencies <br>
* Install the required Python packages: <br>
pip install -r requirements.txt

4. Apply migrations <br>
* Apply migrations to set up the database: <br>
python manage.py migrate

5. Create a superuser (optional for admin access) <br>
python manage.py createsuperuser

6. Run the development server <br>
* Start the Django development server: <br>
python manage.py runserver <br>
* The application should now be accessible at http://127.0.0.1:8000/.

## API Endpoints

Here are the available API endpoints: <br>

### 1. User Authentication <br>
* POST /api/register/: Register a new user. <br>
* POST /api/login/: Log in to an existing account. <br>
* POST /api/logout/: Log out the current user. <br>

### 2. Task Management <br>
* GET /api/tasks/: List all tasks. <br>
* POST /api/tasks/: Create a new task. <br>
* GET /api/tasks/{id}/: Get a single task by ID. <br>
* PUT /api/tasks/{id}/: Update an existing task. <br>
* DELETE /api/tasks/{id}/: Delete a task. <br>

### Task Model Example <br>
{ <br>
  "id": 1, <br>
  "title": "Task Title", <br>
  "description": "Task Description", <br>
  "completed": false, <br>
  "priority": "high", <br>
  "due_date": "2023-12-31T00:00:00Z" <br>
}

### Usage
Once the app is up and running, you can use the API with a tool like Postman, Insomnia, or directly through the frontend (if integrated). Below is a simple example of how to create a task via API:

1. POST /api/tasks/
* Request Body (JSON): <br>
{ <br>
  "title": "Finish Documentation", <br>
  "description": "Write the README for the project", <br>
  "completed": false, <br>
  "priority": "high",<br>
  "due_date": "2023-12-15T00:00:00Z" <br>
}
