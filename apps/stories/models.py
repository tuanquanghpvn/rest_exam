from django.db import models
from apps.categories.models import Category


class Story(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    content = models.TextField()

    class Meta:
        db_table = 'story'

