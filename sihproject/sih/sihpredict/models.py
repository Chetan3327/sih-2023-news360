
from django.db import models


# Create your models here.


class news(models.Model):
    heading=models.TextField()
    content=models.TextField()
    urls=models.TextField()
    source=models.TextField()
    sentiment=models.TextField(null=False , default="neutral")

class newssource(models.Model):
    NewsSource=models.TextField()