from django.contrib import admin
from .models import Post, Comment, Contact
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'post_status', 'created_on', 'updated_on')
    summernote_fields = ('content',)


admin.site.register(Comment)


admin.site.register(Contact)

