from django.shortcuts import get_object_or_404, render, redirect
from slugify import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from blog_app.models import Post, Category
from blog_app.forms import PostForm, SearchForm, CategoryForm


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


# def posts_list(request):
#     posts = Post.objects.filter(publishes=True)
#     context = {
#         'posts': posts
#     }
#     return render(request, 'blog/posts_list.html', context)

class PostListView(ListView):
    model = Post
    template_name = "blog/posts_list.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(publishes=True)


# def post_detail(request, post_slug):
#     post = get_object_or_404(Post, slug=post_slug, publishes=True)
#     # В будущем здесь можно вызывать post.increase_views_count()
#     context = {
#         'post': post}
#     return render(request, 'blog/post_detail.html', context)

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    slug_url_kwarg = 'post_slug'


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


# def post_create(request):
#     if request.method == 'POST':
#         form = PostForm(data=request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.slug = slugify(post.title)
#             post.save()
#             return redirect('blog:index_page')
#     else:
#         form = PostForm()
#     return render(request, "blog/post_create.html", context={'form': form})

class PostFormBase():
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:index_page')

class PostCreateView(PostFormBase, CreateView):
    # model = Post
    # form_class = PostForm
    template_name = 'blog/post_create.html'
    # success_url = reverse_lazy('blog:index_page')

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.slug = slugify(category.title)
            category.save()
            return redirect('blog:categories_list')
    else:
        form = CategoryForm()
    return render(request, "blog/category_create.html", context={'form': form})


# def post_edit(request, post_slug):
#     post = get_object_or_404(Post, slug=post_slug)
#     form = PostForm(data=request.POST or None, instance=post)
#     if request.method == 'POST' and form.is_valid():
#         post.save()
#         return redirect('blog:post_detail', post_slug=post.slug)
#     return render(request, "blog/post_edit.html", context={'form': form})

class PostUpdateView(PostFormBase, UpdateView):
    # model = Post
    # form_class = PostForm
    template_name = "blog/post_edit.html"
    slug_url_kwarg = 'post_slug'
    # success_url = reverse_lazy('blog:index_page')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('blog:index_page')
    slug_url_kwarg = 'post_slug'
