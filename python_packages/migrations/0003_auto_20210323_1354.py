# Generated by Django 3.1.3 on 2021-03-23 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('python_packages', '0002_auto_20210323_0800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='categories',
        ),
        migrations.AddField(
            model_name='category',
            name='packages',
            field=models.ManyToManyField(blank=True, related_name='categories', to='python_packages.Package'),
        ),
    ]