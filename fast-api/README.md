# FastAPI Project

A modern, fast web API built with FastAPI framework.

## Requirements

- Python 3.13 or higher
- FastAPI
- Uvicorn (ASGI server)

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
3. Activate the virtual environment:
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - Unix/MacOS:
     ```bash
     source .venv/bin/activate
     ```
4. Install dependencies:
   ```bash
   pip install -e .
   ```

## Running the Application

Start the server with:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access:
- Interactive API documentation (Swagger UI): `http://localhost:8000/docs`
- Alternative API documentation (ReDoc): `http://localhost:8000/redoc`

## Project Structure

```
fast-api/
├── main.py           # Main application file
├── pyproject.toml    # Project dependencies and metadata
└── README.md         # This file
```
