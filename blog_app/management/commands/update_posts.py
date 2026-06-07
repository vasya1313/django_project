from django.core.management.base import BaseCommand
from blog_app.models import Post


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--post_id', type=int)
        parser.add_argument('--new_title', type=str)

    def handle(self, *args, **options):
        post_id = options['post_id']
        new_title = options['new_title']

        try:
            post = Post.objects.get(id=post_id)
            post.title = new_title
            post.save()
            self.stdout.write(self.style.SUCCESS(f'Пост с ID {post_id} успешно обновлён.'))
        except Post.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Пост с ID {post_id} не найден.'))
