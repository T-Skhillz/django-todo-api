# Todo List API

A Django REST Framework-based API for managing personal todo tasks with JWT authentication.

**🚀 Live API:** [https://django-todo-api-1.onrender.com/](https://django-todo-api-1.onrender.com/)

## Features

- User authentication with JWT tokens (access, refresh, and verify)
- Create, read, update, and delete tasks
- Task categorization (Work, School, Business, Personal, Recreational)
- User-specific task management
- RESTful API architecture

## Tech Stack

- Django 5.2.8
- Django REST Framework
- Simple JWT for authentication
- Python Decouple for environment configuration
- PostgreSQL/MySQL (configurable)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/T-Skhillz/django-todo-api.git
cd django-todo-api
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install django==5.2.8 djangorestframework==3.16.1 djangorestframework-simplejwt==5.5.1 python-decouple==3.8 psycopg2-binary==2.9.10 gunicorn==23.0.0 whitenoise==6.11.0 dj-database-url==3.0.1
```

Or install from requirements.txt:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with the following variables:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_ENGINE=django.db.backends.postgresql
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
```

5. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## API Endpoints

### Authentication

- `POST /api/auth/login/` - Obtain JWT token pair (access & refresh)
- `POST /api/auth/refresh/` - Refresh access token
- `POST /api/auth/verify/` - Verify token validity
- `POST /register/` - Register a new user account

### Tasks

- `GET /` - API root (lists available endpoints)
- `GET /users/` - List all users (authenticated)
- `GET /tasks/` - List all tasks for authenticated user
- `POST /tasks/` - Create a new task
- `GET /tasks/<id>/` - Retrieve a specific task
- `PUT /tasks/<id>/` - Update a specific task
- `DELETE /tasks/<id>/` - Delete a specific task

## Usage Examples

**Note:** The examples below use curl, but you can use any REST client like Thunder Client, Postman, or Insomnia. Just use the same HTTP methods, URLs, headers, and request bodies shown.

**API Base URL:** `https://django-todo-api-1.onrender.com`

### 1. Register a New User

```bash
curl -X POST https://django-todo-api-1.onrender.com/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "newuser",
    "email": "newuser@example.com",
    "password": "securepassword123",
    "password2": "securepassword123"
  }'
```

Response:
```json
{
  "username": "newuser",
  "email": "newuser@example.com"
}
```

### 2. Obtain Access Token

```bash
curl -X POST https://django-todo-api-1.onrender.com/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "your_username", "password": "your_password"}'
```

Response:
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### 3. Create a Task

```bash
curl -X POST https://django-todo-api-1.onrender.com/tasks/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Complete project documentation",
    "category": "work",
    "completed": false
  }'
```

### 4. Get All Tasks

```bash
curl -X GET https://django-todo-api-1.onrender.com/tasks/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### 5. Update a Task

```bash
curl -X PUT https://django-todo-api-1.onrender.com/tasks/1/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Complete project documentation",
    "category": "work",
    "completed": true
  }'
```

### 6. Delete a Task

```bash
curl -X DELETE https://django-todo-api-1.onrender.com/tasks/1/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Task Model

| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Auto-generated primary key |
| user | ForeignKey | Reference to User model |
| title | CharField | Task title (max 300 characters) |
| created_on | DateTimeField | Auto-generated timestamp |
| completed | BooleanField | Task completion status (default: False) |
| category | CharField | Task category (Work/School/Business/Personal/Recreational) |

## Admin Panel

Access the Django admin panel at `https://django-todo-api-1.onrender.com/admin/` to manage tasks and users with a visual interface.

## Deployment

This API is deployed on [Render](https://render.com/) with:
- Automatic deployments from GitHub
- PostgreSQL database
- HTTPS/SSL enabled
- Environment variable management

**Note:** The free tier on Render may sleep after 15 minutes of inactivity. The first request after sleep takes ~30 seconds to wake up.

## Local Development

For local development, use `http://localhost:8000` instead of the production URL.

## Security Notes

- Never commit your `.env` file to version control
- Keep `DEBUG=False` in production
- Use strong, unique secret keys
- Consider enabling SSL for remote database connections (uncomment `sslmode` in settings)
- Implement rate limiting for production environments

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! If you'd like to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature/your-feature`)
6. Open a Pull Request

Please ensure your code follows the existing style and includes appropriate tests.