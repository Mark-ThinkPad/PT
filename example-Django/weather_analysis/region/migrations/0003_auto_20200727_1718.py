# Generated by Django 2.2.14 on 2020-07-27 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0002_auto_20200727_1033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='region',
            name='is_display',
        ),
        migrations.RemoveField(
            model_name='region',
            name='is_municipality',
        ),
        migrations.RemoveField(
            model_name='region',
            name='is_province_capital',
        ),
        migrations.RemoveField(
            model_name='region',
            name='is_province_municipality',
        ),
        migrations.RemoveField(
            model_name='region',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='region',
            name='level',
        ),
        migrations.RemoveField(
            model_name='region',
            name='longitude',
        ),
    ]
