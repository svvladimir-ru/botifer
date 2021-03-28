from django.urls import path
from . import views
from .decorators import check_recaptcha


urlpatterns = [
    # path("signup/", views.SignUp.as_view(), name="signup"),
    path("signup/", check_recaptcha(views.singup), name="signup"),
]