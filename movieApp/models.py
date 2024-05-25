from django.db import models


class MovieData(models.Model):
    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    type = models.CharField(max_length=100, default='action')
    image = models.ImageField(upload_to='Image/', default='Image/None/Noimg.png')

    def __str__(self):
        return self.name