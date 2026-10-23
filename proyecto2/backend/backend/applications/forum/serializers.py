from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import (
    Category,
    Topic,
    Post,
    )

from applications.users.serializers import PublicUserSerializer

class SubcategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "title",
            "description",
            "position",
            "parent_category",
        ]

class CategorySerializer(ModelSerializer):
    subcategories = SerializerMethodField()

    class Meta:
        model = Category
        fields = [
            "id",
            "title",
            "description",
            "subcategories",
            "position",
            "parent_category",
            ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        view = self.context.get("view")

        if view and view.action != "retrieve":
            self.fields.pop("subcategories", None)

    def get_subcategories(self, obj):
        subcategories = Category.objects.filter(parent_category= obj.id)
        return SubcategorySerializer(subcategories, many=True, context=self.context).data

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
    """ parent_post = SerializerMethodField() """
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

"""     def get_parent_post(self, obj):
        if obj.parent_post:
            parent_post = Post.objects.get(id=obj.parent_post.id)
            return parent_post.id
        else:
            return None """

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

