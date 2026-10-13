# Working with Django Models

A self-contained Jupyter notebook and demo project covering Django's ORM and model system.

## Contents

```
05-models-django/
├── django_models_complete_guide.ipynb   ← Main learning notebook (81 cells)
└── demos/
    └── carved_rock/                     ← Full Django demo project
```

## Notebook chapters

| # | Title |
|---|-------|
| 1 | Introduction: ORM and Django Models |
| 2 | Defining Models |
| 3 | Model Field Types (text, numeric, date/time, relationships) |
| 4 | QuerySets — CRUD, filtering, field lookups, relation traversal |
| 5 | Custom Methods, Managers, and Model Inheritance |
| 6 | Migrations — create, run, squash, data migrations |
| 7 | ORM Optimization — `select_related`, `prefetch_related`, raw SQL, transactions |

## Demo project

See [`demos/README.md`](demos/README.md) for setup instructions for the **Carved Rock Fitness** store demo.

## Requirements

```bash
python -m venv venv
source venv/bin/activate
pip install django pillow jupyterlab
```

- Python 3.10+
- Django 4+
