from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from branches.utils import upload_facade_to
from simple_branching.storage_backends import MediaStorage


class Branch(models.Model):
    name = models.CharField(max_length=1000)
    facade = models.ImageField(
        _(u"Facade"),
        storage=MediaStorage(),
        upload_to=upload_facade_to,
        null=True,
        blank=True,
    )
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )

    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )

    class Meta:
        verbose_name_plural = "branches"
        permissions = [("edit_coordinates", "Can edit coordinates")]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("branch-detail", kwargs={"pk": self.pk})
