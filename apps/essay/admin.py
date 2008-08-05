from django.contrib import admin
import models

class EssayAdmin(admin.ModelAdmin):
    list_display = list_display_links = search_fields = (
        'title', 'slug', 'text', )
    prepopulated_fields = { 'slug': ('title', )}
admin.site.register(models.Essay, EssayAdmin)