from django.views.generic import ListView, DetailView

from employees.models import Employee


class EmployeeListView(ListView):
    model = Employee

    def get_queryset(self):
        branch_name = self.request.GET.get("branch_name", None)
        new_context = Employee.objects.all()
        if branch_name:
            new_context = new_context.filter(branch__name=branch_name)
        return new_context

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(EmployeeListView, self).get_context_data(
            object_list=object_list, **kwargs
        )
        context["branch_name"] = self.request.GET.get("branch_name", None)
        return context


class EmployeeDetailView(DetailView):
    model = Employee
