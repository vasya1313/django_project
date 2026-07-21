from django.test import TestCase
from blog_app.models import Category


class CategoryModelCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            title='Тестирование Django',
            slug='django-testing'
        )

    def test_category_fields_creation(self):
        self.assertEqual(self.category.title, 'Тестирование Django')
        self.assertEqual(self.category.slug, 'django-testing')

    def test_category_string_representation(self):
        self.assertEqual(str(self.category), 'Тестирование Django')
