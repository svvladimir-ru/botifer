from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # flatpages
    path("auth/", include("users.urls")),
    path("auth/", include("django.contrib.auth.urls")),
    # импорт из приложения posts
    path("", include("app.urls")),
]
