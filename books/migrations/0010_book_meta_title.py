# Generated by Django 3.1.3 on 2020-12-15 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20201215_0447'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='meta_title',
            field=models.CharField(default='hello', max_length=80),
            preserve_default=False,
        ),
    ]
