import random
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import get_user_model
from .tasks import send_task_email
from rest_framework.authtoken.models import Token


User = get_user_model()
code = random.randint(1000, 9999)


def index(request):
    """Главная страница"""
    return render(request, 'index.html')


def active(request, username, code=code):
    """Страница активации email"""
    user = get_object_or_404(User, username=username)
    send_task_email.delay(user.email, code)
    if request.method == 'POST':
        code_email = request.POST['num']    # получаем код
        if int(code_email) == int(code):
            user = get_object_or_404(User, username=username)
            user.is_staff = True
            user.save()
            return redirect('index')
    return render(request, 'active.html')


def token_api(request, username):
    """Страница просмотра токена"""
    user = get_object_or_404(User, username=username)
    t = Token.objects.get(user=user)

    return render(request, 'get_token.html', {'token': t.key})
