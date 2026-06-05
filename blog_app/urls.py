from django.urls import path
from blog_app import views

app_name = 'blog_app'


urlpatterns = [
    path("", views.index, name="index_page"), # blog:index_page будет доступно в шаблонах
    path("posts/", views.posts_list, name="posts_list"),
    path("posts/<slug:post_slug>/", views.post_detail, name="post_detail"),
    path("categories/", views.categories_list, name="categories_list"),
    path("categories/<slug:category_slug>/", views.category_detail, name="category_detail"),
]
