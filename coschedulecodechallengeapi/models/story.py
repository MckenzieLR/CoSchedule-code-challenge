from django.db import models



class Story(models.Model):
    by = models.CharField(max_length=50)
    title =models.CharField(max_length=100)
    url = models.CharField(max_length=500)
