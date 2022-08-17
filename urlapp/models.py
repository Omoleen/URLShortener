from django.db import models


# Create your models here.
class Urlsmodel(models.Model):
    original = models.URLField()
    shortened = models.CharField(max_length=200)

    def __str__(self):
        return self.original
