# Generated by Django 3.0.7 on 2020-07-07 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='title',
            field=models.CharField(default='none', max_length=200),
        ),
    ]
