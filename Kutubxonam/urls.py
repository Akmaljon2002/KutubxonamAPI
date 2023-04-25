from django.contrib import admin
from django.urls import path, include
from asosiy.views import *
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static


schema_view = get_schema_view(
   openapi.Info(
      title="Kutubxonam",
      default_version='v1',
      description="Yakuniy loyiha uchun",
      # terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact("Akmaljon Fayzullayev, <akmaljonfayzullayev07@gmail.com>"),
      # license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('audios/', AudiosViewSet.as_view()),
    path('audios/<int:pk>/', AudioDetailAPIView.as_view()),
    path('topics/', TopicsAPIView.as_view()),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('docs2/', schema_view.with_ui('redoc', cache_timeout=0)),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
