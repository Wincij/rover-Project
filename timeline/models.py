from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length=120)
    pub_date = models.DateTimeField(null=False)
    body = models.TextField()
    image = models.ImageField(upload_to='images/', max_length = 100)
