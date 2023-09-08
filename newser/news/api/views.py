from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import permissions, viewsets

from ..models import Story
from .permissions import IsOwnerOrReadOnly
from .serializers import StorySerializer


class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    @extend_schema(
        description="List stories with optional type filter",
        parameters=[
            OpenApiParameter("type", OpenApiTypes.STR, OpenApiParameter.QUERY),
        ],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        story_type = self.request.query_params.get("type")

        if story_type == "all":
            return Story.objects.all()
        return Story.objects.filter(type=story_type)
