# Generated by Django 2.2.14 on 2020-08-05 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0005_region_short_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='short_name',
            field=models.CharField(default=models.CharField(max_length=30, verbose_name='区域名称'), max_length=30, verbose_name='区域名称(短)'),
        ),
    ]
