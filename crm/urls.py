from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)  
from .views import (
    StaffViewSet, PositionViewSet, ShiftViewSet,
    StaffShiftViewSet, StaffAttendanceViewSet
)



 
router = DefaultRouter()
router.register('staff', StaffViewSet, basename='staff')
router.register('positions', PositionViewSet, basename='position')
router.register('shifts', ShiftViewSet, basename='shift')
router.register('staff-shifts', StaffShiftViewSet, basename='staffshift')
router.register('attendance', StaffAttendanceViewSet, basename='attendance')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]

