from django.db import models


class TwitterSchedulerModel(models.Model):
    tweet = models.CharField(max_length=240)
    tweet_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
