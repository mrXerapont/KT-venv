from django.contrib import admin

# Register your models here.
from .models import Snd
from .models import Repeat_type

class SndAdmin(admin.ModelAdmin):
    list_display = ('description', 'mailto', 'text', 'dtime', 'repeat')
    list_display_links = ('description', 'mailto', 'text', 'dtime', 'repeat')
    search_fields = ('mailto', 'dtime')

admin.site.register(Snd, SndAdmin)
admin.site.register(Repeat_type)
