# Generated by Django 4.2.3 on 2023-07-12 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_task_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
