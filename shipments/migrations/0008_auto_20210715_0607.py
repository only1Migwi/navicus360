# Generated by Django 3.2.4 on 2021-07-15 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0007_auto_20210715_0546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freightforwarding',
            name='eta',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='freightforwarding',
            name='etd',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
