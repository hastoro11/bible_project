from django.contrib import admin
from .models import ReadingPlan, ReadingPlanDay, ReadingPlanVerse


class ReadingPlanDayInline(admin.TabularInline):
    model = ReadingPlanDay
    extra = 0


@admin.register(ReadingPlan)
class ReadingPlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'start_date', 'end_date', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at', 'start_date']
    search_fields = ['name', 'description', 'user__username']
    date_hierarchy = 'created_at'
    inlines = [ReadingPlanDayInline]


class ReadingPlanVerseInline(admin.TabularInline):
    model = ReadingPlanVerse
    extra = 0


@admin.register(ReadingPlanDay)
class ReadingPlanDayAdmin(admin.ModelAdmin):
    list_display = ['plan', 'day_number', 'date', 'title', 'is_completed', 'completed_at']
    list_filter = ['is_completed', 'date']
    search_fields = ['plan__name', 'title']
    date_hierarchy = 'date'
    inlines = [ReadingPlanVerseInline]


@admin.register(ReadingPlanVerse)
class ReadingPlanVerseAdmin(admin.ModelAdmin):
    list_display = ['day', 'verse', 'order']
    list_filter = ['day__plan']
    search_fields = ['day__plan__name', 'verse__text']
