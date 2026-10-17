# Django Deployment and Maintenance

Covers the full lifecycle of taking a Django application to production and keeping it running: environment configuration, deployment options, error handling and logging, and managing Django and Python upgrades.

All three modules are consolidated into a single notebook: [`django-deployment-maintenance.ipynb`](django-deployment-maintenance.ipynb).

## Modules

| # | Topic |
|---|---|
| 01 | Configuring and Deploying Django Applications |
| 02 | Handling Errors and Bugs |
| 03 | Upgrading Django and Python |

## Assets

The [`assets/`](assets/) directory contains diagrams extracted from the course slides:

- `01-django-release-schedule.png` — Django release schedule timeline
- `02-django-python-compatibility.png` — Django / Python version compatibility matrix
- `03-virtual-environments.png` — Multiple virtual environment isolation diagram

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install jupyter pymupdf pillow
jupyter notebook django-deployment-maintenance.ipynb
```
