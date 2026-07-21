from django.test import TestCase
from blog_app.forms import PostForm
from blog_app.models import Category

class PostFormTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            title='Новости',
            slug='news'
        )

    def test_form_with_valid_data(self):
        form_data = {
            'title': 'Интересный пост',
            'slug': 'interesting-post',
            'content': 'Текст интересного поста.',
            'category': self.category.pk,
            'publishes': True
        }

        form = PostForm(data=form_data)
        self.assertTrue(form.is_valid())


    def test_form_invalid_with_empty_title(self):
        form_data = {
            'title': '',
            'slug': 'empty-title-post',
            'content': 'Текст поста.',
            'category': self.category.pk
        }

        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)


    def test_form_invalid_with_empty_content(self):
        form_data = {
            'title': 'Заголовок поста',
            'slug': 'empty-content-post',
            'content': '',
            'category': self.category.pk
        }

        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors)
