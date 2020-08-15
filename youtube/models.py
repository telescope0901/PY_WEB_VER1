from django.db import models

# Create your models here.

class Youtube(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField('url', unique=True)
    create_date = models.DateTimeField('CreateDate', auto_now_add = True, blank = True, null = True)

    def __str__(self):
        return self.title