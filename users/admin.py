from django.contrib import admin
from .models import Profile


class UserAdmin(admin.ModelAdmin):
    model = Profile
    # search_fields = ('user',)

    empty_value_display = '-пусто-'


admin.site.register(Profile, UserAdmin)
