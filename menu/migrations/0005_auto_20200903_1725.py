# Generated by Django 3.1.1 on 2020-09-03 14:25

import django.core.files.storage
from django.db import migrations, models
import django.utils.timezone
import menu.models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20200903_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='picture',
            field=models.ImageField(default=django.utils.timezone.now, storage=django.core.files.storage.FileSystemStorage(base_url='/media/my_sell/', location='D:\\MyProject\\media/my_sell/'), upload_to=menu.models.image_directory_path),
            preserve_default=False,
        ),
    ]