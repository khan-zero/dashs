from django import forms
from crm.models import Staff, Position, Shift, StaffShift, StaffAttendance


class StaffAttendanceForm(forms.ModelForm):
    class Meta:
        model = StaffAttendance
        fields = ['staff', 'date', 'status']

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['user', 'position', 'is_staff']

class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['name']

class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = ['name', 'start_time', 'end_time']

class StaffShiftForm(forms.ModelForm):
    class Meta:
        model = StaffShift
        fields = ['staff', 'shift', 'date']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = StaffAttendance
        fields = ['staff', 'date', 'status']
