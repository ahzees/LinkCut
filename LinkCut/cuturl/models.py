from django.db import models


# Create your models here.
class Url(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    full_url = models.URLField()
    cut_url = models.CharField(max_length=20)
