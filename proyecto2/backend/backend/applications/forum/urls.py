from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    CategoryViewset,
    EntretementoViewset,
    ArteViewset,
    TopicViewset,
    PostViewset
)

router = DefaultRouter()

router.register(r"category", CategoryViewset, basename="category")
router.register(r"topic", TopicViewset, basename="topic")
router.register(r"post", PostViewset, basename="post")

urlpatterns = [
    path("", include(router.urls))
]
