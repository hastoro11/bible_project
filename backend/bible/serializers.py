from rest_framework import serializers
from .models import Book, Verse, Highlight, Note, ReadingProgress


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'abbreviation', 'testament', 'order', 'chapter_count']


class VerseSerializer(serializers.ModelSerializer):
    book_name = serializers.CharField(source='book.name', read_only=True)
    
    class Meta:
        model = Verse
        fields = ['id', 'book', 'book_name', 'chapter', 'verse_number', 'text']


class HighlightSerializer(serializers.ModelSerializer):
    verse_text = serializers.CharField(source='verse.text', read_only=True)
    verse_reference = serializers.SerializerMethodField()
    
    class Meta:
        model = Highlight
        fields = ['id', 'verse', 'verse_text', 'verse_reference', 'color', 'created_at']
        read_only_fields = ['created_at']
    
    def get_verse_reference(self, obj):
        return f"{obj.verse.book.name} {obj.verse.chapter}:{obj.verse.verse_number}"


class NoteSerializer(serializers.ModelSerializer):
    verse_text = serializers.CharField(source='verse.text', read_only=True)
    verse_reference = serializers.SerializerMethodField()
    
    class Meta:
        model = Note
        fields = ['id', 'verse', 'verse_text', 'verse_reference', 'content', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
    
    def get_verse_reference(self, obj):
        return f"{obj.verse.book.name} {obj.verse.chapter}:{obj.verse.verse_number}"


class ReadingProgressSerializer(serializers.ModelSerializer):
    verse_reference = serializers.SerializerMethodField()
    
    class Meta:
        model = ReadingProgress
        fields = ['id', 'verse', 'verse_reference', 'read_at']
        read_only_fields = ['read_at']
    
    def get_verse_reference(self, obj):
        return f"{obj.verse.book.name} {obj.verse.chapter}:{obj.verse.verse_number}"
