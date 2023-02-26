from rest_framework import generics
from .serializers import RequestSerializer


class RequestCreateView(generics.CreateAPIView):
    "Добавление заявки"
    serializer_class = RequestSerializer
