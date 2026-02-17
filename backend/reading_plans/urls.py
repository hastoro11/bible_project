from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReadingPlanViewSet

router = DefaultRouter()
router.register(r'plans', ReadingPlanViewSet, basename='reading-plan')

urlpatterns = [
    path('', include(router.urls)),
]
