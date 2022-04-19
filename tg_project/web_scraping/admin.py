from django.contrib import admin
from .models import GodURL, BadURL

# Register your models here.

class GodURLAdmin(admin.ModelAdmin):
    pass
admin.site.register(GodURL, GodURLAdmin)

class BadURLAdmin(admin.ModelAdmin):
    pass
admin.site.register(BadURL, BadURLAdmin)