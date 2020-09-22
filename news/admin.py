from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('post_header', 'post_text',
                    'post_author', 'post_date')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_post', 'comment_text', 'comment_date')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
