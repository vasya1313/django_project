from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Ваше имя",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Как к вам обращаться...'
        })
    )

    email = forms.EmailField(
        label="Электронная почта",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'name@example.com'
        })
    )

    subject = forms.ChoiceField(
        label="Тема обращения",
        choices=[
            ('tech', 'Технический вопрос'),
            ('offer', 'Предложения'),
            ('complaint', 'Жалоба'),
            ('other', 'Другое'),
        ],
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    message = forms.CharField(
        label="Ваше обращение",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Опишите ваш вопрос или предложение...',
            'rows': 5
        })
    )
