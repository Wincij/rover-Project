from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length=120)
    pub_date = models.DateField(null=False)
    body = models.TextField()
    image = models.ImageField(upload_to='images/', max_length = 100)

# For readable admin panel and managing
    def __str__(self):
        return self.title


# Convert 01:00 01.01.2000 to January 2000
    def prettyDate(self):
        return self.pub_date.strftime('%B %Y'.upper(), )


# Ordered on timeline.html
    class Meta:
        ordering = ['pub_date']
