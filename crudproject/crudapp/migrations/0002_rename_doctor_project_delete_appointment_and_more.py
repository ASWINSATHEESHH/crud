# Generated by Django 4.2.2 on 2023-06-24 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Doctor',
            new_name='Project',
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]
