from django.db import models
import os
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


image_storage = FileSystemStorage(
    # Physical file location ROOT
    location=u'{0}/my_sell/'.format(settings.MEDIA_ROOT),
    # Url for file
    base_url=u'{0}my_sell/'.format(settings.MEDIA_URL),
)


def image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/my_sell/picture/<filename>
    return u'picture/{0}'.format(filename)


class State(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'States'


class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='Categories'


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class Food(models.Model):
    name=models.CharField(max_length=50)
    desc=models.TextField()
    picture = models.ImageField(upload_to=image_directory_path, storage=image_storage)
    price=models.PositiveIntegerField()
    state=models.ForeignKey('State',on_delete=models.CASCADE,null=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='Food'