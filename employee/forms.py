from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Employee


class EmployeeCreationForm(UserCreationForm):
    class Meta:
        model = Employee
        fields = ("username",)
