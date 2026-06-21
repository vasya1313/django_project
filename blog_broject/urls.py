from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('feedback/', include('feedback_app.urls')),
    path('', include("blog_app.urls", namespace="blog")),
]
