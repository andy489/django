# Carved Rock Fitness — Django Models Demo

Final demo project from the "Working with Django Models" course (Django 5 / Python 3.12).

Covers: model fields, relationships, custom managers, QuerySets, migrations, ORM optimization with `select_related`/`prefetch_related`, and the Django Debug Toolbar.

## Project structure

```
demos/
├── carved_rock/          # Django project root
│   ├── manage.py
│   ├── carved_rock/      # Project settings package
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   ├── store/            # Main app
│   │   ├── models.py     # Product, ProductImage, Category
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── admin.py
│   │   ├── migrations/
│   │   └── templates/
│   ├── fixtures/
│   │   └── my_data.json  # Sample data
│   └── static/
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup

### 1. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate      # macOS/Linux
# venv\Scripts\activate       # Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Apply migrations

```bash
cd carved_rock
python manage.py migrate
```

### 4. Load sample data (optional)

```bash
python manage.py loaddata fixtures/my_data.json
```

### 5. Create a superuser (for admin)

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000 in your browser.
The Django admin is at http://127.0.0.1:8000/admin/.

## Key URLs

| URL | Description |
|-----|-------------|
| `/admin/` | Django admin |
| `/store/filter/` | Product filter page |
| `/store/category/<name>` | Products by category |
| `/store/product/<pk>` | Product detail |
| `/__debug__/` | Django Debug Toolbar (dev only) |

## Models overview

- **Product** — name, price, stock_count, description, sku, slug; custom `ProductInStockQuerySet` manager with `.in_stock()`; auto-slugify on save; `@cached_property` for VAT calculation
- **ProductImage** — image file with ForeignKey to Product (cascade delete)
- **Category** — ManyToMany relationship with Products

## Notable settings

- `ATOMIC_REQUESTS = True` — every request wrapped in a transaction
- SQL query logging enabled in `settings.py` (stdout)
- Django Debug Toolbar enabled for local development
- `crispy-bootstrap5` for form rendering
