from django.urls import path, re_path

from branches.views import BranchListView, BranchDetailView, get_closest_branch

urlpatterns = [
    path("", BranchListView.as_view(), name="branch-list"),
    path("<int:pk>/", BranchDetailView.as_view(), name="branch-detail"),
    re_path(
        r"^(?P<lat>[0-9.]+)/(?P<lng>[0-9.]+)", get_closest_branch, name="closest-branch"
    ),
]
