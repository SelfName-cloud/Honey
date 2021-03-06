# Generated by Django 3.2 on 2021-04-22 12:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20210422_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='social_web',
            field=models.URLField(default=23, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.date(2021, 4, 22)),
        ),
    ]
