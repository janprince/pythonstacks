# Generated by Django 3.1 on 2020-11-11 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package_finder', '0004_package_project_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='top_library',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='resource',
            name='link',
            field=models.URLField(unique=True),
        ),
    ]
