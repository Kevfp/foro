from django.db import models

class CategoryManager(models.Manager):

    def filter_parent_categories(self):
        return self.filter(parent_category=None)