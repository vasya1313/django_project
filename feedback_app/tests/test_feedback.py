from django.test import TestCase
from django.urls import reverse
from feedback_app.models import Feedback


class FeedbackViewTests(TestCase):
    def test_successful_feedback_submission(self):
        initial_feedback_count = Feedback.objects.count()

        form_data = {
            'name': 'Тестовый Пользователь',
            'email': 'test@example.com',
            'subject': 'tech',
            'message': 'Это тестовое сообщение для проверки формы.'
        }

        response = self.client.post(reverse('feedback:feedback_form'), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('feedback:success'))
        self.assertEqual(Feedback.objects.count(), initial_feedback_count + 1)

    def test_feedback_submission_validation_error(self):
        initial_feedback_count = Feedback.objects.count()

        form_data = {
            'name': 'Тестовый Пользователь',
            'email': '',
            'message': 'Сообщение с невалидным email.',
            'subject': 'offer',
        }

        response = self.client.post(reverse('feedback:feedback_form'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Feedback.objects.count(), initial_feedback_count)
        self.assertFormError(response.context['form'], 'email', 'Обязательное поле.')
