from django.db import models
from django.contrib.auth.models import User


class User_path(models.Model):
    """Модель сохранения визита"""
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, null=True)
    pub_date = models.DateTimeField("Дата входа", auto_now_add=True, db_index=True)
    url = models.URLField(default='http://127.0.0.1:8000/api/v1/')

    def __str__(self):
        return self.username
