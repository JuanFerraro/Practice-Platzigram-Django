"""Posts admin clases."""

#Django
from django.contrib import admin

#Models
from posts.models import Post

@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    """Posts admin."""

    list_display = ('pk', 'user', 'photo')
    list_display_links = ('pk', 'user')
    list_editable = ('photo',)
    list_filter = (
                'created',
                'modified'
    )