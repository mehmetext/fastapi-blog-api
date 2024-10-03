# FastAPI Blog API

## Overview

This project is a robust Blog API built with FastAPI, providing a full-featured backend for managing blog posts. It includes features such as creating, reading, updating, and deleting blog posts, along with search functionality and sorting options.

## Features

- CRUD operations for blog posts
- Asynchronous database operations with SQLAlchemy
- Database migrations using Alembic
- Search functionality for posts
- Sorting and filtering options
- Automatic slug generation for posts
- Seeding functionality for development and testing

## Tech Stack

- FastAPI
- SQLAlchemy (Async)
- Alembic
- Pydantic
- PostgreSQL
- Python 3.9+

## Project Structure

The project follows a modular structure:

- `app/`: Main application directory
  - `controllers/`: Business logic
  - `lib/`: Utility functions and configurations
  - `models/`: Database models and Pydantic schemas
  - `routers/`: API route definitions
- `alembic/`: Database migration scripts

## Getting Started

### Prerequisites

- Python 3.9+
- PostgreSQL

### Installation

1. Clone the repository:

   ```
   git clone <repository-url>
   cd <project-directory>
   ```

2. Create and activate a virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory and add the following:

   ```
   APP_NAME=YourAppName
   DB_URL=postgresql+asyncpg://user:password@localhost/dbname
   ```

5. Run database migrations:
   ```
   alembic upgrade head
   ```

### Running the Application

To start the FastAPI server:

```
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

## API Endpoints

- `GET /blog/`: Get all blog posts
- `GET /blog/{id}`: Get a specific blog post
- `POST /blog/`: Create a new blog post
- `PUT /blog/{id}`: Update a blog post
- `DELETE /blog/{id}`: Delete a blog post
- `GET /blog/seed`: Seed the database with sample posts

For detailed API documentation, visit `http://localhost:8000/docs` or `http://localhost:8000/redoc` after starting the server.

## Database Migrations

To create a new migration:

```
alembic revision --autogenerate -m "Description of the change"
```

To apply migrations:

```
alembic upgrade head
```

## Development

### Code Structure

- Models are defined in `app/models/`
- Business logic is in `app/controllers/`
- API routes are defined in `app/routers/`
- Database configurations and sessions are managed in `app/lib/db.py`

### Adding New Features

1. Create or update models in `app/models/`
2. Implement business logic in `app/controllers/`
3. Define new routes in `app/routers/`
4. Update database models and run migrations if necessary

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
