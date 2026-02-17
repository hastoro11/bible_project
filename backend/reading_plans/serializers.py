from rest_framework import serializers
from .models import ReadingPlan, ReadingPlanDay, ReadingPlanVerse
from bible.serializers import VerseSerializer


class ReadingPlanVerseSerializer(serializers.ModelSerializer):
    verse_detail = VerseSerializer(source='verse', read_only=True)
    
    class Meta:
        model = ReadingPlanVerse
        fields = ['id', 'verse', 'verse_detail', 'order']


class ReadingPlanDaySerializer(serializers.ModelSerializer):
    verses = ReadingPlanVerseSerializer(many=True, read_only=True)
    
    class Meta:
        model = ReadingPlanDay
        fields = ['id', 'day_number', 'date', 'title', 'is_completed', 'completed_at', 'verses']


class ReadingPlanSerializer(serializers.ModelSerializer):
    days = ReadingPlanDaySerializer(many=True, read_only=True)
    
    class Meta:
        model = ReadingPlan
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'is_active', 'created_at', 'days']
        read_only_fields = ['created_at']


class ReadingPlanListSerializer(serializers.ModelSerializer):
    days_count = serializers.SerializerMethodField()
    completed_days = serializers.SerializerMethodField()
    
    class Meta:
        model = ReadingPlan
        fields = ['id', 'name', 'description', 'start_date', 'end_date', 'is_active', 'created_at', 'days_count', 'completed_days']
        read_only_fields = ['created_at']
    
    def get_days_count(self, obj):
        return obj.days.count()
    
    def get_completed_days(self, obj):
        return obj.days.filter(is_completed=True).count()
