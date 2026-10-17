from django.contrib import admin
from .models import (
    Category,
    Topic,
    Post,
)

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        list_display = ("title",)

class TopicAdmin(admin.ModelAdmin):
    class Meta:
        list_display = ("title",)

class PostAdmin(admin.ModelAdmin):
    class Meta:
        list_display = (
            "topic",
            "user",
            "created_at",
            )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Post, PostAdmin)