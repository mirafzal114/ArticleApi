from django.contrib import admin
from .models import Tag, Article, Comment, Image

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at',)
    search_fields = ('title', 'content',)
    filter_horizontal = ('tags',)  # Добавляем возможность выбора тегов через интерфейс

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'author', 'created_at',)
    search_fields = ('content',)

admin.register(Image)
