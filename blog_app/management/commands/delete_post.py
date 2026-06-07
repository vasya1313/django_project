from django.core.management.base import BaseCommand

from blog_app.models import Post

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--post_id', type=int)

    def handle(self, *args, **options):
        post_id = options['post_id']
        try:
            Post.objects.get(id=post_id).delete()
            self.stdout.write(self.style.SUCCESS(f'Пост с ID {post_id} успешно удалён.'))
        except Post.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Пост с ID {post_id} не найден.'))
