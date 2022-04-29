from django.db import models

class Article(models.Model):
    # for small strings
    title = models.CharField(max_length=200) 
    # for large strings
    text = models.TextField()
    