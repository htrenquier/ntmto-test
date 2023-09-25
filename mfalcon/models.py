from django.db import models

# Create your models here.
class route(models.Model):
    origin = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    traveltime = models.IntegerField(null=False) # set validators
