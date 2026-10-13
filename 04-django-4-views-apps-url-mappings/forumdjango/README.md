# forumdjango

Demo project for the *Django 4: Views, Apps, and URL Mappings* course.
Covers CBVs, sessions, messages, static files, flatpages, signals, email,
RSS feed, Django Debug Toolbar, and i18n/l10n with Spanish translations.

## Requirements

- Python 3.10+
- See `requirements.txt`

## Setup

```bash
# 1. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Apply migrations
python manage.py migrate

# 4. Create an admin user
python manage.py createsuperuser

# 5. Run the development server
python manage.py runserver
```

## URLs

| URL | Description |
|-----|-------------|
| `http://127.0.0.1:8000/forum/` | Forum index |
| `http://127.0.0.1:8000/forum/latest/posts/` | RSS feed |
| `http://127.0.0.1:8000/pages/` | Flatpages (manage via admin) |
| `http://127.0.0.1:8000/admin/` | Admin interface |
| `http://127.0.0.1:8000/__debug__/` | Django Debug Toolbar |

## Project Structure

```
forumdjango/
├── core/
│   ├── settings.py     ← project configuration
│   ├── urls.py         ← root URL config
│   ├── wsgi.py
│   └── asgi.py
├── forum/
│   ├── models.py       ← Post, Comment
│   ├── views.py        ← FBV + CBVs, sessions, messages, signals, email
│   ├── urls.py         ← app URL patterns
│   ├── forum_feeds.py  ← RSS feed
│   ├── admin.py
│   ├── templates/      ← HTML templates + flatpages template
│   ├── static/         ← CSS
│   └── locale/         ← Spanish translations (.po / .mo)
├── locale/             ← project-level translations
├── manage.py
└── requirements.txt
```

## Compiling Translations

```bash
# After editing .po files:
python manage.py compilemessages
```
