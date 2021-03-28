from django.contrib import admin
from .models import User_path


class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'pub_date', 'url')
    search_fields = ('username',)
    list_filter = ('pub_date',)

    empty_value_display = '-пусто-'


admin.site.register(User_path, UserAdmin)
