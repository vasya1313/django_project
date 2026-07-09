from drf_app.api import PostViewSet, CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView #PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView,
from django.urls import path, include
from rest_framework.routers import DefaultRouter



app_name = 'drf'

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
    # path('posts/', PostListCreateAPIView.as_view(), name='post-list-create'),
    # path('posts/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='post-detail'),
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),
]
