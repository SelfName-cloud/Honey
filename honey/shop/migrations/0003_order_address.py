# Generated by Django 3.2 on 2021-04-16 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_order_number_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]