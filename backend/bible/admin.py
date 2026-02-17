from django.contrib import admin
from .models import Book, Verse, Highlight, Note, ReadingProgress


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'abbreviation', 'testament', 'order', 'chapter_count']
    list_filter = ['testament']
    search_fields = ['name', 'abbreviation']
    ordering = ['order']


@admin.register(Verse)
class VerseAdmin(admin.ModelAdmin):
    list_display = ['book', 'chapter', 'verse_number', 'text_preview']
    list_filter = ['book']
    search_fields = ['text']
    
    def text_preview(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    text_preview.short_description = 'Text Preview'


@admin.register(Highlight)
class HighlightAdmin(admin.ModelAdmin):
    list_display = ['user', 'verse', 'color', 'created_at']
    list_filter = ['color', 'created_at']
    search_fields = ['user__username', 'verse__text']
    date_hierarchy = 'created_at'


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['user', 'verse', 'content_preview', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['user__username', 'verse__text', 'content']
    date_hierarchy = 'created_at'
    
    def content_preview(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    content_preview.short_description = 'Content Preview'


@admin.register(ReadingProgress)
class ReadingProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'verse', 'read_at']
    list_filter = ['read_at']
    search_fields = ['user__username', 'verse__text']
    date_hierarchy = 'read_at'
