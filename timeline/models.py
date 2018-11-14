from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length=120)
    pub_date = models.DateField(null=False)
    body = models.TextField()
    image = models.ImageField(upload_to='images/', max_length = 100)

# For readable admin panel and managing
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['pub_date']
