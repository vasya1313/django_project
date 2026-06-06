from django.core.management.base import BaseCommand
from blog_app.models import Post


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('title', type=str, help='Заголовок поста')
        parser.add_argument('content', type=str, help='Содержание поста')

    def handle(self, *args, **options):
        title = options['title']
        content = options['content']



        post = Post.objects.create(title=title, content=content)
        post.save()
        self.stdout.write(self.style.SUCCESS(f'Пост "{post.title}" успешно создан.'))
