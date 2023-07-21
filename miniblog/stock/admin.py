from django.contrib import admin

from .models import *

class ArtifactAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'summary', 'photo', 'time_create', 'author','is_published' ,'cat')
    list_display_links = ('title', 'summary')
    search_fields = ('title', 'text')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    search_fields = ('name',)



admin.site.register(Artifact, ArtifactAdmin)
admin.site.register(Category, CategoryAdmin)