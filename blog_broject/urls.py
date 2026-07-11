from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from ninja import NinjaAPI
from ninja_app import api


ninja_api = NinjaAPI(
    version='2.0.0',
    title='Блог ниндзя АПИ'
)

ninja_api.add_router('/', api.router)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('feedback/', include('feedback_app.urls')),
    path('', include("blog_app.urls", namespace="blog")),
    path('users/', include('users_app.urls')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/', include('drf_app.urls')),
    path('api/v2/', ninja_api.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
