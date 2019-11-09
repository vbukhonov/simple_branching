from django.conf import settings
from django.contrib import admin

from branches.forms import BranchForm
from branches.models import Branch


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    form = BranchForm
    list_display = ("name", "facade", "latitude", "longitude", "current_employees")
    search_fields = ("name",)

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "facade",
                    "latitude",
                    "longitude",
                    "available_employees",
                )
            },
        ),
    )

    class Media:
        if hasattr(settings, "GOOGLE_MAPS_API_KEY") and settings.GOOGLE_MAPS_API_KEY:
            css = {"all": ("css/admin/location_picker.css",)}
            js = (
                "https://maps.googleapis.com/maps/api/js?key={}".format(
                    settings.GOOGLE_MAPS_API_KEY
                ),
                "js/admin/location_picker.js",
            )

    def current_employees(self, obj):
        employees = obj.employees.all().order_by("last_name")
        if employees.count() > 2:
            employees = list(employees[:2])
            employees.append("...")
        return list(employees)

    current_employees.short_description = "Employees"
