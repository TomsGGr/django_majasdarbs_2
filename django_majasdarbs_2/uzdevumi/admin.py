from django.contrib import admin
from .models import Juzeru_klase


class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(Juzeru_klase, UserAdmin)
