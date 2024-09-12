from django.contrib import admin
from django.urls import path
from .views import home,PositionListView,StaffAttendanceCreateView,StaffAttendanceListView,StaffAttendanceUpdateView

urlpatterns = [
    path('home/',home,name='home'),
    path('posit/',PositionListView.as_view(),name='posit'),
    path('attendance/', StaffAttendanceListView.as_view(), name='attendance_list'),
    path('attendance/new/', StaffAttendanceCreateView.as_view(), name='attendance-create'),
    path('attendance/<int:pk>/edit/', StaffAttendanceUpdateView.as_view(), name='attendance-update'),

]