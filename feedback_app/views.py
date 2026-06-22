from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback


def feedback_view(request):
    # Если пользователь отправил заполненную форму (POST)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            # У обычной формы forms.Form НЕТ метода .save()!
            # Извлекаем очищенные и приведенные к типам данные из cleaned_dataPlease enter some code, or 'exit' (without quotes) to exit.
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')

            # Вручную создаем запись в таблице базы данных через ORM
            Feedback.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )

            # После успешного сохранения перенаправляем на главную
            return redirect('feedback:success')

    # Если пользователь просто зашел на страницу (GET)
    else:
        form = FeedbackForm()

    return render(request, 'feedback/feedback.html', {'form': form})


def feedback_success(request):
    return render(request, 'feedback/success.html')
