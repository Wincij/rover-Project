from django.db import models

class About(models.Model):
    title = models.CharField(max_length = 200)
    body = models.TextField()
    facebook = models.CharField(max_length = 500)

    def __str__(self):
        return self.title
