from django.db import models

from branches.models import Branch


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position_title = models.CharField(max_length=100)
    branch = models.ForeignKey(
        Branch,
        on_delete=models.CASCADE,
        related_name="employees",
        blank=True,
        null=True,
    )

    def __str__(self):
        return "{} {}, {}".format(self.first_name, self.last_name, self.position_title)
