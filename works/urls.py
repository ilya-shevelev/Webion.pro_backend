from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import WorkViewSet


urlpatterns = format_suffix_patterns(
    [
        path("", WorkViewSet.as_view({"get": "list"})),
        path("<int:pk>/", WorkViewSet.as_view({"get": "retrieve"})),
    ]
)
