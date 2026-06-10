from django.shortcuts import get_object_or_404, render

from blog_app.models import Post, Category


def index(request):
    # Получаем 5 последних опубликованных постов
    posts = Post.objects.filter(publishes=True)[:5]
    context = {
        'posts' : posts
    }
    return render(request, 'blog/index.html', context)


def posts_list(request):
    posts = Post.objects.filter(publishes=True)
    context = {
        'posts': posts
    }
    return render(request, 'blog/posts_list.html', context)


def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug, publishes=True)
    post.increase_views_count()
    context = {
        'post': post}
    return render(request, 'blog/post_detail.html', context)


def categories_list(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'blog/categories_list.html', context)


def category_detail(request, category_slug):
      # Безопасно находим категорию
      category = get_object_or_404(Category, slug=category_slug)
      # Выбираем только опубликованные статьи, привязанные к этой категории
      posts = Post.objects.filter(category=category, publishes=True)
      context = {
          'category': category,
          'posts': posts
      }
      return render(request, 'blog/category_detail.html', context)
