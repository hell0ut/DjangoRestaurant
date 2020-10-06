# Generated by Django 3.1.1 on 2020-09-02 12:31

from django.db import migrations, models
import menu.models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20200902_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=menu.models.get_image_path),
        ),
    ]