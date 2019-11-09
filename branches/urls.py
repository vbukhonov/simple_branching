from django.urls import path

from branches.views import BranchListView, BranchDetailView

urlpatterns = [
    path("", BranchListView.as_view(), name="branch-list"),
    path("<slug:pk>/", BranchDetailView.as_view(), name="branch-detail"),
]
