# Django 4 OWASP Secure Coding

Security-focused Django module covering OWASP Top 10 vulnerabilities and secure coding practices using the dot_trade demo application.

## Contents

| File | Description |
|---|---|
| `django4-owasp-secure-coding.ipynb` | Course notebook — OWASP Top 10, Django security features, secure coding patterns |
| `dot_trade/` | Demo trading application with security examples |

## Branches

Each branch covers a specific security topic:

| Branch | Topic |
|---|---|
| `main` | Base application |
| `access_control` | Broken access control prevention |
| `api_and_web_services` | API security and key management |
| `authentication` | Authentication hardening |
| `business_logic_security` | Business logic vulnerability prevention |
| `error_handling_logging` | Secure error handling and logging |
| `file_security` | File upload and path traversal security |
| `hardening` | Django security settings and hardening |
| `input_validation` | Input validation and sanitization |
| `protect_sensitive_data` | Sensitive data exposure prevention |

## Setup

```bash
cd dot_trade/owasp_project
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Prerequisites

- Familiarity with Django fundamentals (modules 01–07)
- Basic understanding of web security concepts
