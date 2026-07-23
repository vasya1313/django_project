from PIL import Image
from django.db import models
from django.contrib.postgres.indexes import GinIndex

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название категории')
    slug = models.SlugField(unique=True)


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок статьи')
    slug = models.SlugField(unique=True)
    content = models.TextField(verbose_name='Содержание статьи')
    publishes = models.BooleanField(default=False, verbose_name='Статус публикации')
    author = models.ForeignKey(to='auth.User', on_delete=models.CASCADE, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    views_count = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='posts', verbose_name='Категория')
    image = models.ImageField(
        upload_to='posts/',
        blank=True, null=True,
        verbose_name='Обложка'
        )


    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        indexes = [
            GinIndex(
                fields=['title', 'content'],
                name='post_title_content_gin',
                opclasses=["gin_trgm_ops", "gin_trgm_ops"]
            )
        ]
        ordering = ['-created_at']



    def increase_views_count(self):
        self.views_count += 1
        self.save()


    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
            super().save(*args, **kwargs)
            if self.image:
                img = Image.open(self.image.path)
                if img.height > 1200 or img.width > 1200:
                    output_size = (1200, 1200)
                    img.thumbnail(output_size)
                    img.save(self.image.path)
