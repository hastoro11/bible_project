from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    """Model representing a book of the Bible"""
    name = models.CharField(max_length=50, unique=True)
    abbreviation = models.CharField(max_length=10)
    testament = models.CharField(max_length=2, choices=[('OT', 'Old Testament'), ('NT', 'New Testament')])
    order = models.IntegerField(unique=True)
    chapter_count = models.IntegerField()
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.name


class Verse(models.Model):
    """Model representing a Bible verse"""
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='verses')
    chapter = models.IntegerField()
    verse_number = models.IntegerField()
    text = models.TextField()
    
    class Meta:
        ordering = ['book__order', 'chapter', 'verse_number']
        unique_together = ['book', 'chapter', 'verse_number']
        indexes = [
            models.Index(fields=['book', 'chapter', 'verse_number']),
        ]
    
    def __str__(self):
        return f"{self.book.name} {self.chapter}:{self.verse_number}"


class Highlight(models.Model):
    """Model for verse highlights"""
    COLOR_CHOICES = [
        ('yellow', 'Yellow'),
        ('green', 'Green'),
        ('blue', 'Blue'),
        ('pink', 'Pink'),
        ('orange', 'Orange'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='highlights')
    verse = models.ForeignKey(Verse, on_delete=models.CASCADE, related_name='highlights')
    color = models.CharField(max_length=10, choices=COLOR_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['user', 'verse']
    
    def __str__(self):
        return f"{self.user.username} - {self.verse} ({self.color})"


class Note(models.Model):
    """Model for verse notes"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    verse = models.ForeignKey(Verse, on_delete=models.CASCADE, related_name='notes')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.verse}"


class ReadingProgress(models.Model):
    """Model for tracking user's reading progress"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reading_progress')
    verse = models.ForeignKey(Verse, on_delete=models.CASCADE)
    read_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-read_at']
        unique_together = ['user', 'verse']
    
    def __str__(self):
        return f"{self.user.username} - {self.verse}"
