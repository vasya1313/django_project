from blog_app.models import Category, Post
from users_app.models import Profile


def categories_processor(request):
    return {
        'nav_categories': Category.objects.all()
    }


def blog_stats_processor(request):
    total_posts = Post.objects.count()
    total_users = Profile.objects.count()
    return {
        'total_posts': total_posts,
        'total_users': total_users,
    }
