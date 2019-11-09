from django.views.generic import DetailView
from django.views.generic.list import ListView

from branches.models import Branch


class BranchListView(ListView):
    model = Branch


class BranchDetailView(DetailView):
    model = Branch
