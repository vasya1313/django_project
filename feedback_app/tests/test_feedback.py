from django.test import TestCase
from django.urls import reverse
from feedback_app.models import Feedback


class FeedbackViewTests(TestCase):
    """Набор тестов для представлений приложения feedback_app."""

    def test_successful_feedback_submission(self):
        """
        Проверяет успешную отправку формы обратной связи, редирект
        и создание объекта Feedback в базе данных.
        """
        initial_feedback_count = Feedback.objects.count()

        form_data = {
            'name': 'Тестовый Пользователь',
            'email': 'test@example.com',
            'subject': 'tech',
            'message': 'Это тестовое сообщение для проверки формы.'
        }

        response = self.client.post(reverse('feedback:feedback_form'), data=form_data)

        # Проверяем, что после успешной отправки происходит редирект
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('feedback:success'))

        # Проверяем, что количество объектов Feedback в базе данных увеличилось на 1
        self.assertEqual(Feedback.objects.count(), initial_feedback_count + 1)

    def test_feedback_submission_validation_error(self):
        """
        Проверяет, что при отправке невалидных данных (пустой email)
        новый объект Feedback не создается, и форма возвращает ошибку.
        """
        initial_feedback_count = Feedback.objects.count()

        form_data = {
            'name': 'Тестовый Пользователь',
            'email': '',  # Невалидное значение
            'message': 'Сообщение с невалидным email.',
            'subject': 'offer',
        }

        response = self.client.post(reverse('feedback:feedback_form'), data=form_data)

        # Проверяем, что страница не была перенаправлена, а осталась с кодом 200
        self.assertEqual(response.status_code, 200)

        # Проверяем, что в базе данных НЕ появился новый объект
        self.assertEqual(Feedback.objects.count(), initial_feedback_count)

        # Проверяем, что форма вернула ошибку для поля 'email'
        self.assertFormError(response, 'form', 'email', 'This field is required.')
