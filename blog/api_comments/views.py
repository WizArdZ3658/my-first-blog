from django.db.models import Q
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)

from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

)

from ..api.permissions import IsOwnerOrReadOnly
from ..api.pagination import PostLimitOffsetPagination, PostPageNumberPagination

from ..models import Comment

from .serializers import (
    CommentListSerializer,
    CommentDetailSerializer,
    # create_comment_serializer
)


# class CommentCreateAPIView(CreateAPIView):
#     queryset = Comment.objects.all()
#
#     def get_serializer_class(self):
#         model_type = self.request.GET.get("type")
#         slug = self.request.GET.get("slug")
#         parent_id = self.request.GET.get("parent_id", None)
#         return create_comment_serializer(
#             model_type=model_type,
#             slug=slug,
#             parent_id=parent_id,
#             user=self.request.user
#         )


class CommentDetailAPIView(RetrieveAPIView):
    queryset = Comment.objects.filter(id__gte=0)
    serializer_class = CommentDetailSerializer
    # permission_classes = [IsOwnerOrReadOnly]
    #
    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    #
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)


class CommentListAPIView(ListAPIView):
    serializer_class = CommentListSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['text', 'author']
    pagination_class = PostPageNumberPagination  # PageNumberPagination

    def get_queryset(self, *args, **kwargs):
        # queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = Comment.objects.all()  # filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(text__icontains=query) |
                Q(author__icontains=query)
            ).distinct()
        return queryset_list
