from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=120)
    blogpost = models.CharField(max_length=500)
    author = models.CharField(max_length=100)

    def _str_(self):
        return self.title