# Generated by Django 3.1.3 on 2021-01-03 17:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_auto_20201216_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='category_images'),
        ),
    ]