from django.contrib import admin
from .models import Bands
# Register your models here.

@admin.register(Bands)
class BandsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'genre')
    list_filter = ('genre',)
    search_fields = ('name',)