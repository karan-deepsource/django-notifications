# -*- coding: utf-8 -*-
import jsonfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notifications", "0002_auto_20150224_1134"),
    ]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="data",
            field=jsonfield.fields.JSONField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
