# Generated by Django 3.1.5 on 2021-02-15 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cohort', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cohort',
            name='uid',
            field=models.UUIDField(blank=True, default=None, null=True, unique=True),
        ),
    ]
