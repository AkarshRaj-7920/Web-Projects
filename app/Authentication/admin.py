from django.contrib import admin
from .models import PasswordReset, Profile

# Register your models here.
admin.site.register(PasswordReset)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)