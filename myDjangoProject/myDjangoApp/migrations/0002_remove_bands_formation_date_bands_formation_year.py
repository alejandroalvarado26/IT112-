# Generated by Django 5.2.1 on 2025-06-13 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myDjangoApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bands',
            name='formation_date',
        ),
        migrations.AddField(
            model_name='bands',
            name='formation_year',
            field=models.IntegerField(default=0),
        ),
    ]
