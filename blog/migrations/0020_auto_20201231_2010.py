# Generated by Django 3.1.3 on 2020-12-31 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20201209_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='overview',
        ),
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
