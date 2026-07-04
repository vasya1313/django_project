from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'social_link', 'avatar']
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Расскажите немного о себе...'
            }),
            'social_link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://example.com/username'
            }),
            # ClearableFileInput добавляет кнопку выбора файла и галочку удаления текущего файла
            'avatar': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }


class CustomLoginForm(AuthenticationForm):
         def __init__(self, *args, **kwargs):
             super().__init__(*args, **kwargs)
             for field_name, field in self.fields.items():
                 field.widget.attrs.update({
                     'class': 'form-control',
                     'placeholder': field.label
                 })


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label
            })
