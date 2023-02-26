from rest_framework import viewsets
from .models import Work
from .serializers import WorkListSerializer, WorkDetailSerializer


class WorkViewSet(viewsets.ReadOnlyModelViewSet):
    "Вывод работ"
    queryset = Work.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return WorkListSerializer
        elif self.action == "retrieve":
            return WorkDetailSerializer
