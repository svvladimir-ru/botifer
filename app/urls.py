from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<username>/', views.active, name='active'),
    path('token/<username>', views.token_api, name='api_token'),
]
