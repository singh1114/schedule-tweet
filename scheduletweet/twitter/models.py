from django.db import models


class TwitterSchedulerModel(models.Model):
    tweet = models.TextField(max_length=240)
    tweet_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    sent = models.BooleanField(default=False)
