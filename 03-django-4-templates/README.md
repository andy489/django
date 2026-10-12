# 03 — Django 4 Templates

Learning material for the **Django 4 Templates** course by Sandy Ludosky.

Covers Django 4.2 template system — DTL syntax, inheritance, composition, custom tags, caching, and Jinja2.

## Contents

| Resource | Description |
|---|---|
| [`django-4-templates-comprehensive.ipynb`](django-4-templates-comprehensive.ipynb) | Comprehensive learning notebook — all 4 modules with explanations and code examples |
| [`demos/`](demos/) | Course demo project source code (Daily News app using the NYT API) |

## Modules

| # | Module | Topics |
|---|---|---|
| 02 | Introduction to Django Templates | MVT architecture, DTL basics, first template, URL routing |
| 03 | Discovering the Power of the Django Template System | Built-in tags, `for`/`if`, built-in filters, static files, API integration |
| 04 | Composing Templates | Template inheritance (`extends`/`block`), fragments (`include`), custom tags/filters, XSS escaping |
| 05 | Optimizing Django Templates | Django Debug Toolbar, `@cache_page`, fragment caching, Jinja2 alternative engine |

## Key Concepts Covered

- MVT (Model–View–Template) architecture
- Django Template Language: `{{ var }}`, `{% tag %}`, `{{ var|filter }}`, `{# comment #}`
- Template inheritance with `{% extends %}` and `{% block %}`
- Reusable fragments with `{% include %}`
- Custom template tags and filters via `templatetags/` package
- Static files with `{% load static %}` and `{% static %}`
- Auto-escaping and XSS protection (`mark_safe`, `| safe`, `| escape`)
- Django Debug Toolbar setup and usage
- View caching (`@cache_page`), low-level caching, fragment caching
- Jinja2 as an alternative template engine

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install django django-debug-toolbar requests
```

To run the demo project:

```bash
cd demos/files/5.4/final/dailynews
python manage.py migrate
python manage.py runserver
```
