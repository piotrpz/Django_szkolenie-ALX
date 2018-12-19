from django.contrib import admin

# Register your models here.

from obrazki.models import Obrazek

@admin.register(Obrazek)
class AdminObrazek(admin.ModelAdmin):
    list_display = ['tytul', 'link_do_obrazka']