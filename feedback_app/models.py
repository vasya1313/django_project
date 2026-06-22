from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя отправителя")
    email = models.EmailField(verbose_name="Email для связи")
    message = models.TextField(verbose_name="Текст сообщения")
    subject = models.CharField(max_length=150, verbose_name="Тема обращения")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправки")


    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Сообщения обратной связи"
        ordering = ["-created_at"]  # Сортировка: новые сообщения вверху


    def __str__(self):
        return f"Сообщение от {self.name} ({self.email}) {self.subject}"
