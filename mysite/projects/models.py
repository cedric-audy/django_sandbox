import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    text = 'test project'
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.text
