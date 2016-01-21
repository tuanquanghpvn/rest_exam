from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)

    class Meta:
        db_table = 'category'
