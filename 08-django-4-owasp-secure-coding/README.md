# Django 4 OWASP Secure Coding

Security-focused Django module covering OWASP Top 10 vulnerabilities and secure coding practices using the dot_trade demo application.

## Contents

| File/Folder | Description |
|---|---|
| `django4-owasp-secure-coding.ipynb` | Course notebook — OWASP Top 10, Django security features, secure coding patterns |
| `dot_trade_main/` | Base dot_trade application |
| `dot_trade_access_control/` | Broken access control prevention |
| `dot_trade_api_and_web_services/` | API security and key management |
| `dot_trade_authentication/` | Authentication hardening |
| `dot_trade_business_logic_security/` | Business logic vulnerability prevention |
| `dot_trade_error_handling_logging/` | Secure error handling and logging |
| `dot_trade_file_security/` | File upload and path traversal security |
| `dot_trade_hardening/` | Django security settings and hardening |
| `dot_trade_input_validation/` | Input validation and sanitization |
| `dot_trade_protect_sensitive_data/` | Sensitive data exposure prevention |
| `dot_trade_secure_sessions/` | Secure session management |

## Setup

```bash
cd dot_trade_<topic>/owasp_project
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Prerequisites

- Familiarity with Django fundamentals (modules 01–07)
- Basic understanding of web security concepts
