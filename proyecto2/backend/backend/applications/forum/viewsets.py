from rest_framework.viewsets import ModelViewSet
from .models import (
    Category,
    Post,
    Topic,
)
from .serializers import (
    CategorySerializer,
    ReadOnlyPostSerializer,
    PostSerializer,
    ReadOnlyTopicSerializer,
    TopicSerializer
)

def _choose_serializer(obj, read_only, writable_serializer, *args, **kwargs):
    if obj.action == 'list' or obj.action == 'retrieve':
        serializer_class = read_only
    else:
        serializer_class = writable_serializer

    return serializer_class(*args, **kwargs)

class CategoryViewset(ModelViewSet):
    queryset = Category.objects.filter_parent_categories()
    serializer_class = CategorySerializer

class PostViewset(ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer(self, *args, **kwargs):     
       return _choose_serializer(self, ReadOnlyPostSerializer, PostSerializer, *args, **kwargs)

class TopicViewset(ModelViewSet):
    queryset = Topic.objects.all()

    def get_serializer(self, *args, **kwargs):
        return _choose_serializer(self, ReadOnlyTopicSerializer, TopicSerializer, *args, **kwargs)