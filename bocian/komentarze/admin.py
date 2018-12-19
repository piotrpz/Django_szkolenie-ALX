from django.contrib import admin

# Register your models here.
from .models import Komentarze

@admin.register(Komentarze)
class AdminKomentarze(admin.ModelAdmin):
        pass