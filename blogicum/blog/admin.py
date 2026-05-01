from django.contrib import admin
from .models import Location, Category, Post


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'is_published', 'category')
    list_filter = ('is_published', 'category', 'pub_date')
    search_fields = ('title', 'text')
    raw_id_fields = ('author', 'location', 'category')
    date_hierarchy = 'pub_date'
