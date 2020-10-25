from django.contrib import admin

from twitter.models import TwitterSchedulerModel

@admin.register(TwitterSchedulerModel)
class TwitterSchedulerAdmin(admin.ModelAdmin):
    list_display = ('tweet', 'tweet_at', 'created_at', 'sent')
    search_fields = ('tweet', 'tweet_at', 'created_at')
