from django.views.generic import ListView, DetailView

from employees.models import Employee


class EmployeeListView(ListView):
    model = Employee


class EmployeeDetailView(DetailView):
    model = Employee
