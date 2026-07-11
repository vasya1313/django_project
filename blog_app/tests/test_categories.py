from django.test import TestCase
from blog_app.models import Category


class CategoryModelCase(TestCase):
    """Набор тестов для модели категорий (Category)."""

    def setUp(self):
        """Создаем категорию для последующих проверок."""
        self.category = Category.objects.create(
            title='Тестирование Django',
            slug='django-testing'
        )

    def test_category_fields_creation(self):
        """Проверяем корректность сохранения всех переданных полей модели."""
        self.assertEqual(self.category.title, 'Тестирование Django')
        self.assertEqual(self.category.slug, 'django-testing')

    def test_category_string_representation(self):
        """Проверяем, что метод __str__ возвращает заголовок категории."""
        self.assertEqual(str(self.category), 'Тестирование Django')
