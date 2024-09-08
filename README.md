# Python FastAPI REST Starter

Kick-starter to your REST application.

## How to set up environment variables?

- Fill the .env file with the following values, they might need adjustment.
  ```dotenv
  DEBUG=<BOOLEAN>                   # Dev: True
  SECRET_KEY=<TOKEN>                # Dev: a1b2c3d4e5f6g7h8i9j10k11l12m13n14o15p16q
  SQLALCHEMY_DATABASE_URI=<STRING>  # Dev: sqlite:///db.sqlite3
  ```

## How to set up project for development?

- Create a virtual environment: -
  ```bash
  python -m venv venv
  ```
- Activate: -
    - Windows: `venv\Scripts\activate`
    - Unix-like: `. venv\bin\activate`
- Install dependencies: -
  ```bash
  pip install . -e '.[all]'
  ```
- Run: -
  ```bash
  uvicorn app.asgi:application --reload
  ```

## How to set up project for deployment?

- Create a virtual environment: -
  ```bash
  python -m venv venv
  ```
- Activate: -
    - Windows: `venv\Scripts\activate`
    - Unix-like: `. venv\bin\activate`
- Install dependencies: -
  ```bash
  pip install -e '.[sqlite,deployment]'
  ```
- Run: -
  ```bash
  gunicorn app:asgi:application -b 0.0.0.0:8000 -w 4 -k uvicorn.workers.UvicornWorker --log-level INFO
  ```
