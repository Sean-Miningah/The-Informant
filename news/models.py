from django.db import models

# Create your models here.

class Story(models.Model):
    Title = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    Datetime = models.DateTimeField(auto_now_add=True)
    source_url = models.URLField(max_length=200)
    img_url = models.URLField(max_length=200, null = True)
    category = models.CharField(max_length=50, null = True) 

    def __str__(self):
        return self.Title 