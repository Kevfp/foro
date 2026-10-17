from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import (
    Category,
    Topic,
    Post,
    )

from applications.users.serializers import PublicUserSerializer

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ReadOnlyTopicSerializer(ModelSerializer):
    category = CategorySerializer()
    user = PublicUserSerializer()
    class Meta:
        model = Topic
        fields = "__all__"

class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"

class ReadOnlyPostSerializer(ModelSerializer):
    topic = ReadOnlyTopicSerializer()
    user = PublicUserSerializer()
    parent_post = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            "topic",
            "user",
            "content",
            "parent_post",
            "created_at",
            "updated_at",
        ]

    def get_parent_post(self, obj):
        if obj.parent_post:
            parent_post = Post.objects.get(id=obj.parent_post.id)
            return parent_post.id
        else:
            return None

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

