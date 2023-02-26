from rest_framework import generics
from .models import Job
from .serializers import JobSerializer


class JobDetailView(generics.RetrieveAPIView):
    "Вывод должности"

    queryset = Job.objects.all()
    serializer_class = JobSerializer
