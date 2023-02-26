from django.db import models


class Review(models.Model):
    """Отзывы"""

    client_name = models.CharField("Имя", max_length=255, null=True, blank=True)
    client_photo = models.ImageField(
        "Фото", upload_to="reviewers_photos", null=True, blank=True
    )
    text = models.TextField("Текст")
    link = models.URLField("URL сайта", null=True, blank=True)
