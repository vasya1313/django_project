from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    # Колонки для отображения в списке сообщений
    list_display = ('name', 'email', 'created_at')
    # Фильтрация по дате отправки сообщения
    list_filter = ('created_at',)
    # Возможность поиска по автору сообщения, email и тексту
    search_fields = ('name', 'email', 'message')
    # Запрещаем редактирование полей обратной связи прямо из админки (readonly)
    readonly_fields = ('name', 'email', 'message', 'created_at')
