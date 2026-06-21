from django.urls import path
from blog_app import views

app_name = 'blog_app'


urlpatterns = [
    path("", views.IndexView.as_view(), name="index_page"), # blog:index_page будет доступно в шаблонах
    path("posts/", views.PostListView.as_view(), name="posts_list"),
    path("posts/create/", views.PostCreateView.as_view(), name="post_create"),
    path('posts/<slug:post_slug>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path("posts/<slug:post_slug>/", views.PostDetailView.as_view(), name="post_detail"),
    path('posts/<slug:post_slug>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path("categories/", views.categories_list, name="categories_list"),
    path("categories/create/", views.category_create, name="category_create"),
    path("categories/<slug:category_slug>/", views.category_detail, name="category_detail"),
]
