from django.db.models import Q
from rest_framework.generics import (ListAPIView,
                                     RetrieveUpdateAPIView,
                                     UpdateAPIView,
                                     DestroyAPIView,
                                     CreateAPIView,
                                     RetrieveAPIView)
from apps.posts.models import Post
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import (PostListSerializer,
                          PostDetailSerializer,
                          PostCreateUpdateSerializer)
from rest_framework.permissions import (
                                    AllowAny,
                                    IsAuthenticated,
                                    IsAdminUser,
                                    IsAuthenticatedOrReadOnly
                                    )
from .permissions import  IsOwnerOrReadOnly
from .pagination import PostLimitOffsetPagination, PostPageNumberPagination



class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostListAPIView(ListAPIView):
    serializer_class = PostListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    permission_classes = [AllowAny]
    search_fields = ['title','text', 'author__first_name']
    pagination_class = PostPageNumberPagination #PageNumberPagination

    def get_queryset(self, *args, **kwargs):
        # queryset_list = super(PostListAPIView, self).get_queryset(*args,**kwargs)
        queryset_list = Post.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(text__icontains=query) |
                Q(author__first_name__icontains=query) |
                Q(author__last_name__icontains=query)
            ).distinct()
        return queryset_list


class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'slug'

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwnerOrReadOnly]


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    permission_classes = [AllowAny]
