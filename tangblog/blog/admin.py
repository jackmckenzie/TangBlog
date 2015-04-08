from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin

from . import models

class PostAdmin(MarkdownModelAdmin):
    list_display = ("title", "publish_on", "created")
    prepopulated_fields = {'slug': ("title",)}

# Register your models here.
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Tag)
