# 01 — Django Big Picture

Three slide decks distilled into a single Jupyter notebook with cleaned diagram assets.

## Contents

```
01-django-big-picture/
├── django_big_picture.ipynb   # comprehensive learning notebook
├── assets/                    # cleaned slide diagrams (noise + logo removed)
│   ├── django_backend_arch-07.png
│   ├── django_features-08.png
│   ├── mtv_pattern-4.png
│   └── request_response_flow-5.png
└── demos/
    └── travel_blog/           # full Django demo project
```

## Notebook Topics

1. **Introducing Django** — what it is, history, backend architecture, built-in features
2. **Structure of a Django Application** — MTV pattern, request/response cycle, models/views/URLs/templates
3. **Choosing Django** — strengths, ecosystem, alternatives (Flask, FastAPI, Laravel, .NET Core)

## Running the Demo

```bash
cd demos/travel_blog
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000` in your browser.

## Running the Notebook

```bash
pip install jupyter pillow
jupyter notebook django_big_picture.ipynb
```
