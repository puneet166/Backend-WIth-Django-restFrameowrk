# Generated by Django 3.0.5 on 2021-05-07 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reg',
            name='FirstName',
        ),
        migrations.RemoveField(
            model_name='reg',
            name='LastName',
        ),
    ]
