from django.db import models

# Create your models here.
# news/models.py


class pttdata(models.Model):
    date = models.TextField()
    author = models.TextField()
    title = models.TextField()
    href = models.TextField()
    pushcount = models.TextField()
    content = models.TextField()
class Meta:
        db_table = "PTT_NEWS"