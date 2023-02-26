from django.db import models
from jobs.models import Job


class Staff(models.Model):
    """Персонал"""

    name = models.CharField("Полное имя", max_length=255)
    image = models.ImageField("Фото", upload_to="staff/", null=True, blank=True)
    job = models.ManyToManyField(Job, verbose_name="Должность")
    email = models.EmailField("Email", null=True, blank=True)
    telegram = models.CharField("Telegram", max_length=255, null=True, blank=True)
    instagram = models.CharField("Instagram", max_length=255, null=True, blank=True)
    facebook = models.CharField("Facebook", max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Персонал"
        verbose_name_plural = "Персонал"
