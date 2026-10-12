from django.shortcuts import render
from common.utils import getResults
from django.views.decorators.cache import cache_page
import config

TOPSTORIES = "https://api.nytimes.com/svc/topstories/v2/arts.json?api-key="
MOSTPOPULAR = "https://api.nytimes.com/svc/mostpopular/v2/emailed/7.json?api-key="
FEED = "https://api.nytimes.com/svc/topstories/v2/world.json?api-key="

links = [
    {"name": "Home", "path": "/"},
    {"name": "Top Stories", "path": "/topstories"},
    {"name": "Most Popular", "path": "/popular"},
    {"name": "Real Time Feed", "path": "/feed"}
]

apis = [
    {"name": "Top Stories API", "path": "/topstories"},
    {"name": "Most Popular API", "path": "/popular"},
    {"name": "Times Wire API", "path": "/feed"},
]


def index(request):
    return render(request, 'articles/index.html', {'title': 'Daily News', })


@cache_page(600)
def home(request):
    return render(request, 'articles/home.html', {'title': 'Daily News', "apis": apis})


def results(request):
    pathname = str(request).split("/").pop(1)
    results = []
    subtitle = ""

    if (pathname == "topstories"):
        results = getResults(TOPSTORIES + config.api_key)
        subtitle = "Top"
    elif (pathname == "popular"):
        results = getResults(MOSTPOPULAR + config.api_key)
        subtitle = "Most Popular"
    elif (pathname == "feed"):
        results = getResults(FEED + config.api_key)
        subtitle = "Feed"
    else:
        return

    return render(request, 'articles/results.html', {'title': 'Daily News', 'subtitle': subtitle, "results": results, "links": links, "pathname": pathname + "/"})
