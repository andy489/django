# Daily News

A Django app that aggregates news from the New York Times API.

## Getting a NYT API Key

1. Go to [https://developer.nytimes.com](https://developer.nytimes.com)
2. Click **Sign In** → **Create Account**
3. After logging in, go to **My Apps** → **+ New App**
4. Give your app a name and enable the following APIs:
   - **Top Stories API**
   - **Most Popular API**
5. Click **Save** — your API key will be displayed on the app page

## Setup

```bash
# Clone and enter the project
cd 03-django-4-templates/dailynews

# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create a .env file with your API key
echo "NYT_API_KEY=your_api_key_here" > .env

# Run the development server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

## Features

- **Top Stories** — Arts section top stories
- **Most Popular** — Most emailed articles (last 7 days)
- **Real Time Feed** — World top stories
- Django Debug Toolbar for development
- Jinja2 and Django template engine support
- Per-endpoint response caching
