from django.db import models

# Create your models here.


class QueryResult(models.Model):
    sno = models.AutoField(primary_key=True)
    video_url = models.URLField()
    channel_name = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    thumbnail_url = models.URLField()
    publish_time = models.DateField()

    def __str__(self):
        return self.title
