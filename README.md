# Todo List API

A Django REST Framework-based API for managing personal todo tasks with JWT authentication.

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
pip install django djangorestframework djangorestframework-simplejwt python-decouple psycopg2-binary
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

### 1. Obtain Access Token

```bash
curl -X POST http://localhost:8000/api/auth/login/ \
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

### 2. Create a Task

```bash
curl -X POST http://localhost:8000/tasks/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Complete project documentation",
    "category": "work",
    "completed": false
  }'
```

### 3. Get All Tasks

```bash
curl -X GET http://localhost:8000/tasks/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### 4. Update a Task

```bash
curl -X PUT http://localhost:8000/tasks/1/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Complete project documentation",
    "category": "work",
    "completed": true
  }'
```

### 5. Delete a Task

```bash
curl -X DELETE http://localhost:8000/tasks/1/ \
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

Access the Django admin panel at `http://localhost:8000/admin/` to manage tasks and users with a visual interface.

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