from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from users_app.models import Profile


class ProfileTests(TestCase):
    """Набор тестов для профиля пользователя."""

    def setUp(self):
        """Создаем пользователя для тестов."""
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_profile_is_created_on_user_creation(self):
        """
        Проверяет, что сигнал post_save для модели User
        автоматически создает объект Profile.
        """
        self.assertTrue(Profile.objects.filter(user=self.user).exists(),
                        "Профиль не был создан для нового пользователя.")
        self.assertIsNotNone(self.user.profile,
                             "Атрибут 'profile' не доступен у объекта пользователя.")

    def test_profile_edit_page_redirects_anonymous_user(self):
        """
        Проверяет, что неавторизованный пользователь перенаправляется
        со страницы редактирования профиля на страницу входа.
        """
        profile_update_url = reverse('users:profile_edit')
        login_url = reverse('users:login')
        response = self.client.get(profile_update_url)
        self.assertRedirects(response, f'{login_url}?next={profile_update_url}')

    def test_profile_edit_page_accessible_for_authenticated_user(self):
        """
        Проверяет, что авторизованный пользователь может успешно
        открыть страницу редактирования своего профиля.
        """
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('users:profile_edit'))
        self.assertEqual(response.status_code, 200)
