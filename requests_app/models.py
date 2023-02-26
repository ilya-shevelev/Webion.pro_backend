from django.db import models


class Request(models.Model):
    """Заявки"""

    email = models.EmailField("Email")
    name = models.CharField("Имя", max_length=255, blank=True, null=True)
    text = models.TextField("Текст")
    date = models.DateTimeField("Дата и время", auto_now_add=True)

    def __str__(self):
        return f"{self.email} - {self.date}"

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
