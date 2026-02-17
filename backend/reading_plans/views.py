from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import ReadingPlan, ReadingPlanDay
from .serializers import ReadingPlanSerializer, ReadingPlanListSerializer, ReadingPlanDaySerializer


class ReadingPlanViewSet(viewsets.ModelViewSet):
    """ViewSet for managing reading plans"""
    
    def get_queryset(self):
        # In a real app, filter by authenticated user
        return ReadingPlan.objects.prefetch_related('days', 'days__verses').all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ReadingPlanListSerializer
        return ReadingPlanSerializer
    
    def perform_create(self, serializer):
        # In a real app, set user from request.user
        from django.contrib.auth.models import User
        user = User.objects.first()
        if not user:
            user = User.objects.create_user('demo_user', password='demo123')
        serializer.save(user=user)
    
    @action(detail=True, methods=['post'])
    def complete_day(self, request, pk=None):
        """Mark a day as completed"""
        day_id = request.data.get('day_id')
        if not day_id:
            return Response({'error': 'day_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            plan = self.get_object()
            day = plan.days.get(id=day_id)
            day.is_completed = True
            day.completed_at = timezone.now()
            day.save()
            
            serializer = ReadingPlanDaySerializer(day)
            return Response(serializer.data)
        except ReadingPlanDay.DoesNotExist:
            return Response({'error': 'Day not found'}, status=status.HTTP_404_NOT_FOUND)
