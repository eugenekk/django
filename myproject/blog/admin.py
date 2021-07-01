from django.contrib import admin
from .models import Post, Comment, Tag

# Register your models here.
admin.site.register(Post) # admin 페이지에서 Post 테이블 관리할 수 있게 등록
admin.site.register(Comment)
admin.site.register(Tag)