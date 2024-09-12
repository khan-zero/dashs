from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from crm.models import Staff, Position, Shift, StaffShift, StaffAttendance,User
from .forms import StaffForm, PositionForm, ShiftForm, StaffShiftForm, StaffAttendanceForm
from django.db.models import Q
from django.views import  View
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

def home(request):
    return render(request,'index.html')

class PositionListView(View):
    def get(self, request):
        positions = Position.objects.all()
        return render(request, 'positions.html', context={'positions': positions})

class StaffAttendanceListView(ListView):
    model = StaffAttendance
    template_name = 'attendance_list.html'
    context_object_name = 'attendances'

    def get_queryset(self):
        return StaffAttendance.objects.all()

class StaffAttendanceCreateView(CreateView):
    model = StaffAttendance
    form_class = StaffAttendanceForm
    template_name = 'attendance_form.html'
    success_url = reverse_lazy('attendance-list')

    def form_valid(self, form):
        # Optionally, you can perform additional logic here
        return super().form_valid(form)

class StaffAttendanceUpdateView(UpdateView):
    model = StaffAttendance
    form_class = StaffAttendanceForm
    template_name = 'attendance_form.html'
    success_url = reverse_lazy('attendance-list')

    def get_object(self, queryset=None):
        # Fetch attendance by staff and date, or ID
        return get_object_or_404(StaffAttendance, pk=self.kwargs.get('pk'))