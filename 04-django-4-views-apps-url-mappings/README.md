# Django 4: Views, Apps, and URL Mappings

## Contents

```
04-django-4-views-apps-url-mappings/
├── forumdjango/                              ← complete demo project
│   ├── manage.py
│   ├── core/                                 ← project settings and root URL config
│   ├── forum/                                ← app with models, views, feeds, templates, i18n
│   ├── requirements.txt
│   └── README.md
├── django_4_views_apps_url_mappings.ipynb    ← self-contained Jupyter Notebook
├── assets/diagrams/                          ← architecture diagram PNGs
└── README.md                                 ← this file
```

## Quick Start — Demo Project

```bash
cd forumdjango
python -m venv .venv
source .venv/bin/activate
pip install django django-debug-toolbar
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit `http://127.0.0.1:8000/forum/` to see the app.  
Visit `http://127.0.0.1:8000/admin/` to manage posts and flatpages.

## Quick Start — Course Notebook

```bash
pip install jupyter pillow matplotlib
jupyter notebook django_4_views_apps_url_mappings.ipynb
```

Run the first cell (Setup: Diagram Renderer) before any other cell.

## Demo Project Features (forumdjango)

| Feature | Where |
|---------|-------|
| `Post` / `Comment` models with timestamps | `forum/models.py` |
| Function-based view (`index`) | `forum/views.py` |
| `ListView`, `DetailView`, `TemplateView` CBVs | `forum/views.py` |
| URL patterns (`path`, `re_path`) + RSS feed route | `forum/urls.py` |
| Sessions and Django Messages framework | `forum/views.py` |
| Static files (`styles.css`, `{% load static %}`) | `forum/static/`, `forum/templates/` |
| Flatpages (`django.contrib.flatpages`) | `core/settings.py`, `forum/templates/flatpages/` |
| Signals + email via console backend | `forum/views.py`, `core/settings.py` |
| RSS/Atom feed (`LatestPostFeed`) | `forum/forum_feeds.py` |
| Django Debug Toolbar | `core/settings.py`, `core/urls.py` |
| i18n / l10n with Spanish translations | `core/settings.py`, `forum/locale/`, `locale/` |

## Modules Covered

| Module | Topic |
|--------|-------|
| 02 | Django architecture: MVT vs MVC |
| 03 | Creating a Django project and app |
| 04 | URL mappings in detail |
| 05 | Built-in view types (FBV, CBV, mixins, decorators, pagination) |
| 06 | Interactivity: sessions, messages, static files |
| 07 | Convenience features: flatpages, signals, email, feeds, debug toolbar |
| 08 | Internationalization and localization |

## Prerequisites

- Python 3.10+
- Basic Python (functions, classes, modules)
- Basic HTML and SQL
