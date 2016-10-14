from __future__ import unicode_literals

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    date = models.DateTimeField()

    def __unicode__(self):
        return u"%s - %s" % (self.title, self.date)
