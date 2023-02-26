from rest_framework import serializers
from .models import Staff
from jobs.serializers import JobSerializer


class StaffSerializer(serializers.ModelSerializer):
    job = JobSerializer(many=True)

    class Meta:
        model = Staff
        exclude = ("name_ru", "name_en")
