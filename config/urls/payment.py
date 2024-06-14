"""
URL Configuration for slu/payment service.
"""

from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView

urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularRedocView.as_view(url_name="schema"), name="docs"),
    path("api/", include("slu.payment.urls")),
    path("", include("slu.payment.service.urls")),
]
