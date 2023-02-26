from rest_framework import serializers
from .models import Work, WorkImage


class WorkImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkImage
        fields = ("image",)


class WorkListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ("id", "main_image")


class WorkDetailSerializer(serializers.ModelSerializer):
    images = WorkImageSerializer(many=True)

    class Meta:
        model = Work
        exclude = (
            "name_ru",
            "name_en",
            "description_ru",
            "description_en",
            "client_ru",
            "client_en",
            "client_photo",
        )
