# Generated by Django 2.2.7 on 2019-11-10 16:20

import branches.utils
from django.db import migrations, models
import simple_branching.storage_backends


class Migration(migrations.Migration):

    dependencies = [("branches", "0002_auto_20191109_2302")]

    operations = [
        migrations.AlterField(
            model_name="branch",
            name="facade",
            field=models.ImageField(
                blank=True,
                null=True,
                storage=simple_branching.storage_backends.MediaStorage(),
                upload_to=branches.utils.upload_facade_to,
                verbose_name="Facade",
            ),
        )
    ]
