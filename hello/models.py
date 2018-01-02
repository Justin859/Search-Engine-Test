from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    user = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __unicode__(self):
        return self.title
# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)
