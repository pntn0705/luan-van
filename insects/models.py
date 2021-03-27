from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Insect(models.Model):
    name = models.CharField(max_length=100)
    eName = models.CharField(max_length=100)
    slug = models.SlugField()
    detail = models.TextField()
    thump = models.ImageField(default='default.png', blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def snippet(self):
        return self.detail[:50] + '...'


class Insect_Image(models.Model):
    insect = models.ForeignKey(Insect, default=None, on_delete=models.PROTECT)
    image = models.ImageField(default=None, blank=True)
    placeholder = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.image.url


class Rect(models.Model):
    image = models.ForeignKey(
        Insect_Image, default=None, on_delete=models.PROTECT)
    name = models.CharField(max_length=100, default=None)
    x = models.FloatField()
    y = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()

    def __str__(self):
        return 'rect_' + self.image.image.url


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # custom some fields

    def __str__(self):
        return self.user.Username
