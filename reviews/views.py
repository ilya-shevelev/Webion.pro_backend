from rest_framework import generics
from .models import Review
from .serializers import ReviewSerializer


class ReviewListView(generics.ListAPIView):
    "Вывод отзывов"

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
