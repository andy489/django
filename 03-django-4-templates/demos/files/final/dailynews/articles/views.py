from django.shortcuts import render
from django.http import HttpResponse

# https://docs.djangoproject.com/en/4.1/topics/http/views/


def home(request):
    html = "<html><body><h1 style='text-align: center; color: #2980b9;'>Daily News</h1></body></html>"
    return HttpResponse(html)

# def home(request):
#     return render(request, 'articles/home.html', {'title': 'Daily News'})
