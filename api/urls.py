from django.urls import path
from .views import APIUser


urlpatterns = [
    path('<username>', APIUser.as_view(), name='users'),
]
