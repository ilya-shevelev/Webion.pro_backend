from django.urls import path
from .views import RequestCreateView


urlpatterns = [
    path("", RequestCreateView.as_view()),
]
