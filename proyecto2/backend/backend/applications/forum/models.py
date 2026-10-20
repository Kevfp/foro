from django.db import models
from applications.users.models import User
from .managers import CategoryManager

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True, max_length=255)
    parent_category = models.ForeignKey("self", on_delete=models.CASCADE, verbose_name="parent category", null=True, blank=True)
    position = models.PositiveBigIntegerField()

    objects = CategoryManager()

    class Meta:
        verbose_name = "category"
        verbose_name_plural= "categories"
        db_table = "categories"

    def __str__(self):
        return f"{self.title}"

class Topic(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    is_pinned = models.BooleanField()
    is_locked = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "topic"

    def __str__(self):
        return f"{self.title}"

class Post(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=255)
    parent_post = models.ForeignKey("self", on_delete=models.CASCADE, verbose_name="parent post", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "post"

    def __str__(self):
        return f"{self.topic} - {self.user} - {self.created_at}"



