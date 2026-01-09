# Quiz Master - V1

## Project Description

Quiz Master - V1 is a web-based exam preparation platform where admins create and manage subjects, chapters, and quizzes, while users can register, take quizzes, and track their scores. Users can attempt quizzes from various subjects, view past performances, and improve over time. Admins have full control over content, including adding, editing, and organizing quizzes. The platform ensures a structured and engaging learning experience with score tracking and analytics. Built using Flask, Jinja2, Bootstrap, and SQLite for seamless functionality.

## Tech-Stack

### Frontend

- HTML, CSS - For a responsive and user-friendly UI.
- JavaScript - Frontend interactivity and dynamic content.
- Chart.js- Generates quiz performance charts and analytics.
- Jinja2 - Templating engine for dynamic HTML rendering.

### Backend

- Flask - Backend framework for handling requests and routing.
- Flask-SQLAlchemy - ORM for managing the SQLite database.
- Flask-Login- Handles user authentication and session management.
- Werkzeug- Provides secure password hashing and authentication utilities.

### Database

- SQLite- Lightweight database for storing quizzes and user data.

## Installation

#### Create a New virtual environment

```
python -m venv .venv
```

#### Activate the virtual environment

```
source .venv/bin/activate
```

#### Install all the depedenices

```
pip install -r requirements.txt
```

#### Run the app

```
flask run
```
