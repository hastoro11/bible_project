from django.db import models
from django.contrib.auth.models import User
from bible.models import Verse


class ReadingPlan(models.Model):
    """Model representing a reading plan"""
    name = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reading_plans')
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.user.username}"


class ReadingPlanDay(models.Model):
    """Model representing a day in a reading plan"""
    plan = models.ForeignKey(ReadingPlan, on_delete=models.CASCADE, related_name='days')
    day_number = models.IntegerField()
    date = models.DateField()
    title = models.CharField(max_length=200, blank=True)
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['plan', 'day_number']
        unique_together = ['plan', 'day_number']
    
    def __str__(self):
        return f"{self.plan.name} - Day {self.day_number}"


class ReadingPlanVerse(models.Model):
    """Model linking verses to a reading plan day"""
    day = models.ForeignKey(ReadingPlanDay, on_delete=models.CASCADE, related_name='verses')
    verse = models.ForeignKey(Verse, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['day', 'order']
        unique_together = ['day', 'verse']
    
    def __str__(self):
        return f"{self.day} - {self.verse}"
