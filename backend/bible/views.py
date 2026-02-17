from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import Book, Verse, Highlight, Note, ReadingProgress
from .serializers import (
    BookSerializer, VerseSerializer, HighlightSerializer,
    NoteSerializer, ReadingProgressSerializer
)


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for viewing books of the Bible"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    @action(detail=True, methods=['get'])
    def chapters(self, request, pk=None):
        """Get chapter information for a book"""
        book = self.get_object()
        return Response({
            'book': book.name,
            'chapter_count': book.chapter_count,
            'chapters': list(range(1, book.chapter_count + 1))
        })


class VerseViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for viewing Bible verses"""
    queryset = Verse.objects.select_related('book').all()
    serializer_class = VerseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['text', 'book__name']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Filter by book
        book_id = self.request.query_params.get('book', None)
        if book_id:
            queryset = queryset.filter(book_id=book_id)
        
        # Filter by chapter
        chapter = self.request.query_params.get('chapter', None)
        if chapter:
            queryset = queryset.filter(chapter=chapter)
        
        return queryset
    
    @action(detail=False, methods=['get'])
    def search(self, request):
        """Search verses by text"""
        query = request.query_params.get('q', '')
        if not query:
            return Response({'error': 'Search query is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        verses = Verse.objects.filter(text__icontains=query).select_related('book')[:100]
        serializer = self.get_serializer(verses, many=True)
        return Response(serializer.data)


class HighlightViewSet(viewsets.ModelViewSet):
    """ViewSet for managing verse highlights"""
    serializer_class = HighlightSerializer
    
    def get_queryset(self):
        # In a real app, filter by authenticated user
        # For now, return all highlights
        return Highlight.objects.select_related('verse', 'verse__book').all()
    
    def perform_create(self, serializer):
        # In a real app, set user from request.user
        # For now, using first user or anonymous
        from django.contrib.auth.models import User
        user = User.objects.first()
        if not user:
            user = User.objects.create_user('demo_user', password='demo123')
        serializer.save(user=user)


class NoteViewSet(viewsets.ModelViewSet):
    """ViewSet for managing verse notes"""
    serializer_class = NoteSerializer
    
    def get_queryset(self):
        # In a real app, filter by authenticated user
        return Note.objects.select_related('verse', 'verse__book').all()
    
    def perform_create(self, serializer):
        # In a real app, set user from request.user
        from django.contrib.auth.models import User
        user = User.objects.first()
        if not user:
            user = User.objects.create_user('demo_user', password='demo123')
        serializer.save(user=user)


class ReadingProgressViewSet(viewsets.ModelViewSet):
    """ViewSet for managing reading progress"""
    serializer_class = ReadingProgressSerializer
    
    def get_queryset(self):
        # In a real app, filter by authenticated user
        return ReadingProgress.objects.select_related('verse', 'verse__book').all()
    
    def perform_create(self, serializer):
        # In a real app, set user from request.user
        from django.contrib.auth.models import User
        user = User.objects.first()
        if not user:
            user = User.objects.create_user('demo_user', password='demo123')
        serializer.save(user=user)
