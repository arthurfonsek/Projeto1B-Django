from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tag = models.CharField(max_length=200)
    def __str__(self):
        return self.title

