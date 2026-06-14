from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def landing_view(request: HttpRequest) -> HttpResponse:
    return render(request, "tracker/landing.html")
