from django.db import models



class Story(models.Model):
    id = models.AutoField(primary_key=True)
    by = models.CharField(max_length=50)
    title =models.CharField(max_length=100)
    url = models.CharField(max_length=500)
    text = models.CharField(max_length=500)
