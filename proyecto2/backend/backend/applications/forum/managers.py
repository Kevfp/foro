from django.db import models

class CategoryManager(models.Manager):

    def filter_parent_categories(self):
        return self.filter(parent_category=None)

    def filter_entretemento(self):
        return self.filter(parent_category=1)
    
    def filter_arte(self):
        return self.filter(parent_category=2)