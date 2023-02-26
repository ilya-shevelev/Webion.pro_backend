from rest_framework import generics
from .serializers import StaffSerializer
from .models import Staff


class StaffListView(generics.ListAPIView):
    "Вывод списка персонала"
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
