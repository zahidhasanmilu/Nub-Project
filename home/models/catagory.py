from django.db import models
from autoslug import AutoSlugField


class Catagory(models.Model):
    name = models.CharField(max_length=100)


    @staticmethod
    def get_all_catagories():
        return Catagory.objects.all()

    def __str__(self):
        return self.name
