from django.shortcuts import get_object_or_404, render, redirect
from slugify import slugify

from blog_app.models import Post, Category
from blog_app.forms import PostForm, SearchForm


def index(request):
    search_form = SearchForm(data=request.GET)
    # Получаем 5 последних опубликованных постов
    posts = Post.objects.filter(publishes=True)
    if search_form.is_valid():
        query = search_form.cleaned_data.get('query')
        posts = posts.filter(title__icontains=query)
    posts = posts[:5]
    context = {
        'posts' : posts,
        'search_form' : search_form
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
    # В будущем здесь можно вызывать post.increase_views_count()
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


def post_create(request):
    if request.method == 'POST':
        form = PostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.title)
            post.save()
            return redirect('blog:index_page')
    else:
        form = PostForm()
    return render(request, "blog/post_create.html", context={'form': form})
