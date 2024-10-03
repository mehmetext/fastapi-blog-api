# FastAPI Blog API Project

This project is a web application built using FastAPI, a modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints.

## Project Overview

This project was created to learn how to use Python's FastAPI library.

## Requirements

The project requires the following dependencies:

```
fastapi
uvicorn[standard]
```

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/mehmetext/fastapi-blog-api.git
   cd fastapi-blog-api
   ```

2. Create and activate a virtual environment:

   ```
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

3. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   uvicorn main:app --reload
   ```

This will start the server, and you can access the API documentation at `http://127.0.0.1:8000/docs` or `http://127.0.0.1:8000/redoc`.

## Contributing

Contributions to this project are welcome. Please ensure you follow the existing code style and add appropriate tests for new features.
