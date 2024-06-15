from django.contrib import admin

from news.models import Post, Profile

from markdownx.admin import MarkdownxModelAdmin

# Register your models here.

class PostAdmin(MarkdownxModelAdmin):
    list_display = ('id', 'title', 'author',)

admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(Profile)