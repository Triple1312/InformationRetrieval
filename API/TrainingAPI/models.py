from django.db import models

# Create your models here.


class Document(models.Model):
    title = models.CharField(max_length=200, primary_key=True)
    location = models.CharField(max_length=200)
    abstract = models.TextField()

    def __str__(self):
        return self.title
