from django.db import models




class Supporter(models.Model):
    name = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='images/supporters')
    website = models.CharField(max_length = 200)


# For readable admin panel and managing
    def __str__(self):
        return self.name
