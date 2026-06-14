from django.urls import path
from .views.landing import landing_view

urlpatterns = [
    path("", landing_view, name="landing"),
]
