from django.contrib import admin
from .models import Post, Comment, Contact, Like
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'post_status', 'created_on', 'updated_on')
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'posted_on')
    readonly_fields = ('posted_on',)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'reacted_on')
    readonly_fields = ('reaction',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email_address', 'contacted_on')
    readonly_fields = ('contacted_on',)
