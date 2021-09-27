# Generated by Django 3.1.2 on 2021-05-12 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('python_packages', '0006_package_meta_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='package',
            name='homepage',
            field=models.URLField(blank=True, max_length=300),
        ),
    ]