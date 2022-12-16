from django.db import models
from datetime import datetime as dt


class MessagesModel(models.Model):
    user_id = models.IntegerField(blank=False)
    user_to_id = models.IntegerField(blank=False)
    username = models.CharField(max_length=100)
    message = models.CharField(max_length=6000, blank=False, unique=False, editable=True)
    date = models.DateTimeField(blank=True, null=True, default=dt.utcnow())

    def __str__(self): return self.message
