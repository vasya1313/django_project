from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from blog_app.models import Post, Category


def index(request):
    return HttpResponse("<h1>Hello World!</h1>")


def posts_list(request):
    posts = Post.objects.filter(publishes=True)

    content = "<h1>Опубликованные статьи</h1><br><br>"
    for post in posts:
        content += f"<a href='/posts/{post.slug}/'>{post.title}</a> ({post.created_at:%Y-%m-%d})<br>"

    return HttpResponse(content)


def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    content = f'''
        <h1>{post.title}</h1>
        <p>{post.author}</p>
        <div>{post.content}</div>
        <hr>
        <a href="/posts/">Назад к статьям</a>
        '''

    return HttpResponse(content)


def categories_list(request):
    categories = Category.objects.all()

    content = "<h1>Категории постов:</h1><ul>"
    for category in categories:
        content += f"<li><a href='/categories/{category.slug}/'>{category.title}</a></li>"
    content += "</ul>"

    return HttpResponse(content)

def category_detail(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = Post.objects.filter(category=category, publishes=True)

    content = "<h1>Опубликованные статьи</h1><br><br>"
    for post in posts:
        content += f"<a href='/posts/{post.slug}/'>{post.title}</a> ({post.created_at:%Y-%m-%d})<br>"
    content += "<hr>"
    content += "<a href='/categories/'>Назад к категориям</a>"
    return HttpResponse(content)
