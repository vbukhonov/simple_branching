from django import forms

from branches.models import Branch
from employees.models import Employee


class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = "__all__"

    available_employees = forms.ModelMultipleChoiceField(
        queryset=Employee.objects.all(), required=False
    )

    def __init__(self, *args, **kwargs):
        super(BranchForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields["available_employees"].initial = self.instance.employees.all()

    def save_m2m(self):
        pass

    def save(self, *args, **kwargs):
        self.fields["available_employees"].initial.update(branch=None)
        branch_instance = Branch()
        branch_instance.pk = self.instance.pk
        branch_instance.name = self.instance.name
        branch_instance.facade = self.instance.facade
        branch_instance.latitude = self.instance.latitude
        branch_instance.longitude = self.instance.longitude
        branch_instance.save()
        self.cleaned_data["available_employees"].update(branch=branch_instance)
        return branch_instance
