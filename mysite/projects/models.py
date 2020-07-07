import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, default='none')
    text = models.CharField(max_length=200, default='none')
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.text
