from django.db import models
from django.utils import timezone

class DocsLinux(models.Model):
    title = models.CharField(max_length=255)
    ptit = models.CharField(max_length=255)
    pptit = models.CharField(max_length=255)
    pptit = models.CharField(max_length=255)
    content = models.TextField()
    hits = models.IntegerField(default=0)
    def __str__(self):
        return self.title