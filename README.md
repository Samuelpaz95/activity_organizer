# Awikly-backend

This is a project for awikly-backend

- Language: python3.10
- Librery: fastapi
- Path: awikly-backend/main.py

# start awikly-backend

- create virtual environment

```bash
python3.10 -m venv env
```

- activate virtual environment

```bash
source env/bin/activate
```

- activate virtual environment on windows

```cmd
.\env\Scripts\activate
```

- install dependencies

```bash
pip install -r requirements.txt
```

- freeze requirements

```bash
pip freeze > requirements.txt
```

- run awikly-backend

```bash
uvicorn main:app --reload
```
- go to http://localhost:8000/
