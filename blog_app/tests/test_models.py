from django.test import TestCase
from django.contrib.auth.models import User
from blog_app.models import Category, Post


class PostModelCase(TestCase):
    """Набор тестов для модели статей (Post)."""
    def setUp(self):
        self.user = User.objects.create_user(
            username='writer',
            password='Password123'
        )
        # Создаем категорию для последующих проверок
        self.category = Category.objects.create(
            title='Django Тестирование',
            slug='django-testing'
        )
        # Создаем статью для последующих проверок
        self.post = Post.objects.create(
            title='Тестирование в Django',
            slug='testing-in-django',
            content='Тестирование в Django - это важная часть разработки веб-приложений.',
            category=self.category,
            author=self.user,
            publishes=True
        )


    def test_post_fields_creation(self):
        """Проверяем корректность сохранения всех переданных полей модели."""
        self.assertEqual(self.post.title, 'Тестирование в Django')
        self.assertEqual(self.post.slug, 'testing-in-django')
        self.assertEqual(self.post.content, 'Тестирование в Django - это важная часть разработки веб-приложений.')
        self.assertEqual(self.post.category, self.category)
        self.assertEqual(self.post.author, self.user)
        self.assertTrue(self.post.publishes)


    # def test_post_string_representation(self):
    #     """Проверяем, что метод __str__ возвращает заголовок статьи."""
    #     self.assertEqual(str(self.post), 'Тестирование в Django')


    def test_post_published_default_value(self):
        """Убеждаемся, что по умолчанию статья создается неопубликованной (черновиком)."""
        draft_post = Post.objects.create(
            title='Черновик статьи',
            slug='draft-post',
            content='Этот пост не должен быть опубликован сразу.',
            category=self.category,
            author=self.user
            # Поле published не передаем — проверяем значение по умолчанию
        )
        self.assertFalse(draft_post.publishes)
