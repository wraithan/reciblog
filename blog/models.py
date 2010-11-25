from django.db import models

# Create your models here.
class Entry(models.Model):
    class Status:
        LIVE = 1
        PENDING = 2
        CHOICES = (
            (LIVE, 'Live'),
            (PENDING, 'Pending'),
            )
    name = models.CharField(max_length=256)
    content = models.TextField()
    status = models.IntegerField(choices=Status.CHOICES, default=Status.PENDING)
