from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'language', 'isbn']
    list_filter = ['isbn']
    search_fields = ['title']
    list_per_page = 10

@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'dob', 'dod']
    search_fields = ['first_name', 'last_name']

@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(models.BookImage)
class BookImageAdmin(admin.ModelAdmin):
    list_display = ['image', 'book']
    list_display_links = ['image']


admin.site.register(models.BookInstance)

# admin.site.register(models.Book)
# admin.site.register(models.Genre)
# admin.site.register(models.Language)
