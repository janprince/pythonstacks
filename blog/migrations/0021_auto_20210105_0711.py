# Generated by Django 3.1.3 on 2021-01-05 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20201231_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='meta_description',
            field=models.CharField(blank=True, max_length=162),
        ),
    ]
