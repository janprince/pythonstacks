# Generated by Django 3.1.3 on 2020-12-15 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20201215_0425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='download_link',
            field=models.URLField(unique=True),
        ),
    ]
