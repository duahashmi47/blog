from django.contrib import admin

from .models import Post, Category, Comment

class CommentItemInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['post']

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'created_at', 'status')
    list_filter = ('category', 'created_at', 'status')
    search_fields = ('title','intro', 'content')
    ordering = ('-created_at',)
    inlines = [CommentItemInline]
    prepopulated_fields = {'slug': ('title',)} 


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created_at')
    list_filter = ('post', 'created_at')
    search_fields = ('name', 'content')

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
