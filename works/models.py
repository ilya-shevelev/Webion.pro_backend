from django.db import models


class Work(models.Model):
    """Работы"""

    name = models.CharField("Название", max_length=255)
    description = models.TextField("Описание", blank=True, null=True)
    url = models.URLField("URL-адрес")
    client = models.CharField("Клиент", max_length=255, blank=True, null=True)
    main_image = models.ImageField("Главное изображение", upload_to="works_main_images")
    date = models.DateField("Дата", auto_now_add=True)

    def __str__(self):
        return f"{self.url} - {self.name}"

    class Meta:
        verbose_name = "Работа"
        verbose_name_plural = "Работы"


class WorkImage(models.Model):
    """Изображение работы"""

    image = models.ImageField("Изображение", upload_to="works_images/")
    work = models.ForeignKey(
        Work, verbose_name="Работа", on_delete=models.CASCADE, related_name="images"
    )

    def __str__(self):
        return f"{self.work.url} - {self.work.name}"

    class Meta:
        verbose_name = "Изображение работы"
        verbose_name_plural = "Изображения работы"
