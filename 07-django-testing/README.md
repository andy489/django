# Django 4 Testing

A self-contained Jupyter notebook covering Django's testing ecosystem from TDD basics through full integration testing with Selenium.

## Contents

```
07-django-testing/
├── django4-testing.ipynb            ← Main learning notebook
└── assets/
    └── transaction_comparison.png   ← TestCase vs TransactionTestCase diagram
```

## Notebook chapters

| # | Title | Topics |
|---|-------|--------|
| 1 | Test Driven Development (TDD) | Red-Green-Refactor cycle, benefits, TDD in practice |
| 2 | Django Testing Tools Overview | Built-in tools, running tests, test database |
| 3 | The Test Case Class Hierarchy | `SimpleTestCase`, `TestCase`, `TransactionTestCase`, `LiveServerTestCase` |
| 4 | Code Coverage | `coverage` install, reports, `.coveragerc`, targets |
| 5 | Incremental Improvement Strategy | Small → expand → integration cycle |
| 6 | What Should Be Tested | Models, forms, views, custom code — prioritisation |
| 7 | Testing Models | Field constraints, `__str__`, custom methods |
| 8 | Testing Forms | Valid/invalid data, `clean_*`, ModelForm `save()` |
| 9 | Testing Views — with Client | GET/POST, status codes, templates, `reverse()` |
| 10 | Testing Views — with RequestFactory | Bypassing middleware, unit-level view tests |
| 11 | Testing Views — with LiveServerTestCase | Selenium skeleton, when to use |
| 12 | Testing Best Practices | Naming, determinism, isolation, assertions |
| 13 | Managing Test Data | Inline, `setUp`, `setUpTestData` |
| 14 | Working with Fixtures | JSON fixtures, `dumpdata`, `loaddata`, tradeoffs |
| 15 | Transaction Tests | `TransactionTestCase`, `on_commit`, truncate vs rollback |
| 16 | Full Integration Testing with Selenium | Selectors, waits, headless Chrome |
| 17 | Final Coverage Check and Workflow | CI config, test file organisation, class choice matrix |
| 18 | Reference Tables | Class comparison, assertion methods, coverage commands |
| 19 | Exercises | 6 practical exercises with answers |
| 20 | Final Assessment | 10 Q&A covering all modules |

## Requirements

```bash
pip install django jupyterlab coverage selenium
```

- Python 3.10+
- Django 4.2+

## Opening the notebook

```bash
jupyter lab django4-testing.ipynb
```

Or open directly in VS Code with the Jupyter extension.
