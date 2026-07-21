from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from blog_app.models import Category, Post

class AuthorizationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='editor',
            password='securepassword123',
            is_staff=True
        )
        self.category = Category.objects.create(
            title='Базы данных',
            slug='database'
        )


    def test_create_post_anonymous_redirect(self):
        response = self.client.get(reverse('blog:post_create'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/users/login/', response.url)


    def test_create_post_page_accessible_for_authenticated_users(self):
        # Авторизуем пользователя в нашем виртуальном браузере
        self.client.login(username='editor', password='securepassword123')
        response = self.client.get(reverse('blog:post_create'))
        self.assertEqual(response.status_code, 200)


    def test_create_post_via_post_request(self):
        self.client.login(username='editor', password='securepassword123')
        response = self.client.post(reverse('blog:post_create'), data={
            'title': 'Пост созданный в тесте',
            'slug': 'post-sozdannyi-v-teste',
            'content': 'Контент созданный с помощью автотеста.',
            'category': self.category.pk,
            'published': True
        })

        self.assertEqual(response.status_code, 302)
        post_exists = Post.objects.filter(slug='post-sozdannyi-v-teste').exists()
        self.assertTrue(post_exists)
