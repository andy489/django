# Django 4 Forms and ModelForms — Course Notebook

A self-contained Jupyter notebook learning resource covering Django's form and ModelForm system, derived from 52 course slides across 4 modules.

## Contents

```
course_material/
├── course.ipynb          ← Main learning notebook (33 cells)
├── assets/
│   └── diagrams/         ← 14 extracted PNG diagrams
├── README.md             ← This file
├── source_coverage.md    ← PDF → notebook section mapping
└── validation_report.md  ← Completeness and validation checks
```

## Requirements

```bash
pip install django pillow matplotlib
```

- Python 3.10+
- Django 4.2
- Pillow (for diagram rendering in notebook)
- Matplotlib (for diagram rendering in notebook)

## Opening the notebook

```bash
# Install Jupyter if needed
pip install jupyterlab

# Launch from the course_material directory
cd course_material
jupyter lab course.ipynb
```

Or open `course.ipynb` directly in VS Code with the Jupyter extension.

## First steps

1. Open `course.ipynb`.
2. Run the first cell ("Environment setup") to load `render_diagram()`.
3. Proceed through chapters in order — each chapter is self-contained but concepts build progressively.

## Chapters

| # | Title | Topics |
|---|-------|--------|
| 1 | Django Project Structure | File layout, versions |
| 2 | What Is a Django Form? | Form vs ModelForm, bound vs unbound |
| 3 | The Django Form Lifecycle | GET/POST flow, view skeleton, template |
| 4 | Form Field Validation Chain | to_python → clean sequence |
| 5 | Building a Basic Form | Field types, widgets, rendering options |
| 6 | Building a ModelForm | Meta class, save(), field mapping |
| 7 | The ModelForm Validation Chain | full_clean, validate_unique |
| 8 | Built-in Validators | RegexValidator, EmailValidator, etc. |
| 9 | CSRF Security | Attack flow, token protection, troubleshooting |
| 10 | Custom Validation Methods | clean_field, clean() |
| 11 | Form Lifecycle Method Overrides | Signatures, where to put logic |
| 12 | Customising Form Appearance | Widget attrs, CSS, static files |
| 13 | Handling Validation Errors | errors dict, add_error, templates |
| 14 | Enhancing User Experience | Widget reference, __init__ styling, testing |
| 15 | Reference Tables | Quick-reference comparisons |
| 16 | Exercises | 5 practical exercises with answers |
| 17 | Final Assessment | 10 Q&A covering all modules |

## Diagrams

Diagrams are rendered inline using `render_diagram()`. All images are stored locally in `assets/diagrams/` and use relative paths — the notebook works offline and can be moved to any directory as long as the `assets/` folder stays alongside `course.ipynb`.

## Source material

Derived from 4 PDF slide decks (52 pages total):
- Module 2: Creating and Handling Forms (16 pages)
- Module 3: Ensuring Data Integrity and Security (13 pages)
- Module 4: Managing Form Validation Errors (12 pages)
- Module 5: Enhancing User Experience (11 pages)

See `source_coverage.md` for page-level traceability.
