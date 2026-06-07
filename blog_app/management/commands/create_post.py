from django.core.management.base import BaseCommand
from django.utils.text import slugify

from blog_app.models import Post


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--title', type=str)
        parser.add_argument('--content', type=str)
        parser.add_argument('--author_id', type=int, default=1)
        parser.add_argument('--category_id', type=int, default=1)


    def handle(self, *args, **options):
        title = options['title']
        content = options['content']

        # Если слаг не передан, берем заголовок.
        # allow_unicode=True обязателен для поддержки русского языка

        slug = slugify(options['title'], allow_unicode=True)


        author_id = options['author_id']
        category_id = options['category_id']


        post = Post.objects.create(
            title=title,
            content=content,
            slug=slug,
            author_id=author_id,
            category_id=category_id
            )

        self.stdout.write(self.style.SUCCESS(f'Пост "{post.title}" успешно создан!'))
