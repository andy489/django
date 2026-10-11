# 02 — Django Fundamentals

Learning material for the **Django Fundamentals** module.

Covers Django 6.x with Python 3.10+. Builds a **Meeting Planner** web application end-to-end across 8 modules.

## Contents

| Resource | Description |
|---|---|
| [`django-fundamentals.ipynb`](django-fundamentals.ipynb) | Comprehensive learning notebook — all 8 modules with explanations, code examples, and diagrams |
| [`django-fundamentals/`](django-fundamentals/) | Final demo project source code |

## Modules

| # | Module | Code snapshot |
|---|---|---|
| 2 | Starting a Django Project | [`after-module-2-starting-a-django-project/`](after-module-2-starting-a-django-project/) |
| 3 | Creating a Simple Web Page | [`after-module-3-creating-a-simple-web-page/`](after-module-3-creating-a-simple-web-page/) |
| 4 | Setting Up a Data Model | [`after-module-4-setting-up-a-data-model/`](after-module-4-setting-up-a-data-model/) |
| 5 | Combining Model, View and Template | [`after-module-5-combining-model-view-and-template/`](after-module-5-combining-model-view-and-template/) |
| 6 | URLs and Link Building | [`after-module-6-urls-and-link-building/`](after-module-6-urls-and-link-building/) |
| 7 | Templates, Styling and Static Content | [`after-module-7-templates-styling-and-static-content/`](after-module-7-templates-styling-and-static-content/) |
| 8 | Adding User Interaction with ModelForms | [`after-module-8-adding-user-interaction-with-modelforms/`](after-module-8-adding-user-interaction-with-modelforms/) |
| 9 | Editing Meetings and Authentication | [`after-module-9-editing-meetings-and-authentication/`](after-module-9-editing-meetings-and-authentication/) |

## Key Concepts Covered

- Project and app structure (`startproject`, `startapp`)
- Model–Template–View (MTV) architecture
- Django ORM: model classes, migrations, QuerySets
- URL routing with `path()`, `include()`, named URLs
- Django template language: variables, tags, filters, inheritance, static files
- ModelForms: `modelform_factory`, GET/POST pattern, CSRF protection
- Authentication: `@login_required`, built-in login/logout views
- Django Admin configuration

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install django
```

To run a module snapshot:

```bash
cd after-module-9-editing-meetings-and-authentication/meeting_planner
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
