# Django 4 Forms and ModelForms

A self-contained Jupyter notebook covering Django's form and ModelForm system.

## Contents

```
06-django-forms-modelforms/
├── django4-forms-and-modelforms.ipynb   ← Main learning notebook
└── assets/
    └── diagrams/                        ← 14 PNG diagrams rendered inline
```

## Notebook chapters

| # | Title | Topics |
|---|-------|--------|
| 1 | Django Project Structure | File layout, versions |
| 2 | What Is a Django Form? | Form vs ModelForm, bound vs unbound |
| 3 | The Django Form Lifecycle | GET/POST flow, view skeleton, template |
| 4 | Form Field Validation Chain | `to_python` → `clean` sequence |
| 5 | Building a Basic Form | Field types, widgets, rendering options |
| 6 | Building a ModelForm | Meta class, `save()`, field mapping |
| 7 | The ModelForm Validation Chain | `full_clean`, `validate_unique` |
| 8 | Built-in Validators | `RegexValidator`, `EmailValidator`, etc. |
| 9 | CSRF Security | Attack flow, token protection, troubleshooting |
| 10 | Custom Validation Methods | `clean_field`, `clean()` |
| 11 | Form Lifecycle Method Overrides | Signatures, where to put logic |
| 12 | Customising Form Appearance | Widget attrs, CSS, static files |
| 13 | Handling Validation Errors | `errors` dict, `add_error`, templates |
| 14 | Enhancing User Experience | Widget reference, `__init__` styling, testing |
| 15 | Reference Tables | Quick-reference comparisons |
| 16 | Exercises | 5 practical exercises with answers |
| 17 | Final Assessment | 10 Q&A covering all modules |

## Requirements

```bash
pip install django pillow matplotlib jupyterlab
```

- Python 3.10+
- Django 4.2+

## Opening the notebook

```bash
jupyter lab django4-forms-and-modelforms.ipynb
```

Or open directly in VS Code with the Jupyter extension.
