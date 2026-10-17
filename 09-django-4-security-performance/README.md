# Django 4 Security and Performance

A practical guide to securing and optimizing Django 4 applications. Covers SSL/HTTPS configuration, CSRF protection, SQL injection prevention, clickjacking defenses, host header validation, user-uploaded content verification, caching strategies (Memcached, Redis), database query optimization, and template rendering performance.

All modules are consolidated into a single notebook: [`django-4-security-performance.ipynb`](django-4-security-performance.ipynb)

## Modules

| # | Topic |
|---|---|
| 01 | Introducing the Django Framework — setup, virtual environments, deploying to cloud |
| 02 | Ensuring Security in Django 4 — SSL/HTTPS, CSRF, SQLi, clickjacking, host headers, file uploads |
| 03 | Optimizing Django 4 for Speed and Scalability — caching, query optimization, template performance, Memcached |
| 04 | Conclusion and Next Steps |

## Assets

The `assets/` directory contains educational diagrams extracted from the course slides:

- `01-csrf-attack-flow.png` — CSRF attack flow showing attacker, malicious page, and victim interactions
- `02-template-system-pipeline.png` — Django template system pipeline: Configure → Compile → Render

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install jupyter
jupyter notebook django-4-security-performance.ipynb
```
