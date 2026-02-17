from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, VerseViewSet, HighlightViewSet, NoteViewSet, ReadingProgressViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'verses', VerseViewSet, basename='verse')
router.register(r'highlights', HighlightViewSet, basename='highlight')
router.register(r'notes', NoteViewSet, basename='note')
router.register(r'progress', ReadingProgressViewSet, basename='progress')

urlpatterns = [
    path('', include(router.urls)),
]
