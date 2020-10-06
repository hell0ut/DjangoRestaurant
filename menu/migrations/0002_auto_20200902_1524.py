# Generated by Django 3.1.1 on 2020-09-02 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='food',
            options={'verbose_name_plural': 'Food'},
        ),
        migrations.AlterModelOptions(
            name='state',
            options={'verbose_name_plural': 'States'},
        ),
        migrations.AlterField(
            model_name='food',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
