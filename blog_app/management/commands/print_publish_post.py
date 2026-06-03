from django.core.management.base import BaseCommand
from blog_app.models import Post


class Command(BaseCommand):
    def handle(self, *args, **options):
        posts = Post.objects.filter(publishes=True)

        if not posts.exists():
            self.stdout.write(self.style.WARNING("Опубликованных статей нет!"))
            return

        for post in posts:
            self.stdout.write(f'{post.id}: {post.title} - {post.created_at:%Y-%m-%d}')

        self.stdout.write(self.style.NOTICE(f'Найдено опубликованных постов: {posts.count()}'))
