# Generated by Django 3.1.5 on 2021-03-01 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cohort', '0002_cohort_uid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cohort',
            name='cohortName',
        ),
        migrations.AddField(
            model_name='cohort',
            name='cohortName',
            field=models.ManyToManyField(blank=True, related_name='cohort', to='cohort.CohortName'),
        ),
    ]
