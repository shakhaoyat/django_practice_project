# Generated by Django 5.0.8 on 2025-01-17 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='cls',
            new_name='Cls',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='roll',
            new_name='Roll',
        ),
    ]
