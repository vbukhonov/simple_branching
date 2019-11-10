from django.views.generic import ListView, DetailView

from employees.models import Employee


class EmployeeListView(ListView):
    model = Employee

    def get_queryset(self):
        branch_name = self.request.GET.get("branch_name", None)
        new_context = Employee.objects.all()
        if branch_name:
            new_context = new_context.filter(branch__name=branch_name)
        order_by_fields = self.request.GET.get("order_by_fields", None)
        if order_by_fields:
            order_by_fields = order_by_fields.split(",")
            if set(order_by_fields).issubset(
                set([field.name for field in Employee._meta.fields])
            ):
                new_context = new_context.order_by(*order_by_fields)
        return new_context

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(EmployeeListView, self).get_context_data(
            object_list=object_list, **kwargs
        )
        context["branch_name"] = self.request.GET.get("branch_name", None)
        order_by_fields = self.request.GET.get("order_by_fields", None)
        if order_by_fields:
            order_by_fields = order_by_fields.replace(",", ", ")
        context["order_by_fields"] = order_by_fields
        return context


class EmployeeDetailView(DetailView):
    model = Employee
