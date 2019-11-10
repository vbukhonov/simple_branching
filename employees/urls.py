from django.urls import path

from employees.views import EmployeeDetailView, EmployeeListView

urlpatterns = [
    path("", EmployeeListView.as_view(), name="employee-list"),
    path("<int:pk>/", EmployeeDetailView.as_view(), name="employee-detail"),
]
