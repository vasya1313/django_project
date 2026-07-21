from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from blog_app.models import Post, Category
from rest_framework_simplejwt.tokens import RefreshToken


class PostAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.refresh = RefreshToken.for_user(self.user)
        self.access_token = str(self.refresh.access_token)

        self.category = Category.objects.create(title='Тестовая категория', slug='test-category')
        Post.objects.create(
            title='Тестовый пост',
            content='Содержимое тестового поста',
            category=self.category,
            author=self.user
        )


    def test_get_posts_list(self):
        url = reverse('drf:post-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


    def test_create_post_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        url = reverse('drf:post-list')
        data = {
            'title': 'Новый пост от авторизованного пользователя',
            'content': 'Текст нового поста.',
            'category': self.category.pk
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Post.objects.filter(title=data['title']).exists())


    def test_create_post_anonymous(self):
        url = reverse('drf:post-list')
        data = {
            'title': 'Пост от анонима',
            'content': 'Этот пост не должен быть создан.',
            'category': self.category.pk
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
