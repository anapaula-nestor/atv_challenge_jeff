from django.db import models
from challenge.category.models import Category


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=250, null=False, blank=False)
    price = models.FloatField(null=False, default=0)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return f'{self.name} - {self.description}'

    def get_categories(self):
        return "\n".join([c.name for c in self.category.all()])
