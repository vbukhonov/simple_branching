from decimal import Decimal

from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView

from branches.models import Branch
from branches.utils import get_dist_between_points


class BranchListView(ListView):
    model = Branch


class BranchDetailView(DetailView):
    model = Branch


def get_closest_branch(request, lat, lng):
    lat = Decimal(lat)
    lng = Decimal(lng)
    closest_branch = Branch.objects.all().first()
    if closest_branch is not None:
        min_dist = get_dist_between_points(
            coordinates_1=(lat, lng),
            coordinates_2=(closest_branch.latitude, closest_branch.longitude),
        )
        for branch in Branch.objects.all():
            current_dist = get_dist_between_points(
                coordinates_1=(lat, lng),
                coordinates_2=(branch.latitude, branch.longitude),
            )
            if current_dist < min_dist:
                min_dist = current_dist
                closest_branch = branch
    return render(
        request,
        "branches/closest_branch_detail.html",
        {"branch": closest_branch, "lat": lat, "lng": lng},
    )
