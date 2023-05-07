from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Post(models.Model):
    name = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='images')
    url = models.URLField(max_length = 200, default=None, null=True, blank=True)