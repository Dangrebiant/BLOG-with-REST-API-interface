from django.db.models import Q
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import (
	DestroyAPIView,
	ListAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	UpdateAPIView,
	CreateAPIView,
	)

from rest_framework.pagination import(
	LimitOffsetPagination,
	PageNumberPagination,
	)
from rest_framework.permissions import(
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)

from .permissions import IsOwnerOrReadOnly

from posts.models import Post
from .serializers import (
	PostCreateSerializer,
	PostDetailSerializer,
	PostListSerializer,
	)

class PostCreateAPIView(CreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostCreateSerializer
	permission_classes = [IsAuthenticated]
	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

	

class PostDeleteAPIView(DestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostListSerializer  
	lookup_field = 'pk'

class PostDetailAPIView(RetrieveAPIView):
	queryset = Post.objects.all()
	permission_classes = [AllowAny]
	serializer_class = PostDetailSerializer
	lookup_field = 'pk'

class PostListAPIView(ListAPIView):
	queryset = Post.objects.all()
	permission_classes = [AllowAny]
	serializer_class = PostListSerializer
	lookup_field = 'pk'
	pagination_class = LimitOffsetPagination

class PostUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostListSerializer
	permission_classes = [IsOwnerOrReadOnly]
	lookup_field = 'pk'

	def perform_update(self, serializer):
		serializer.save(user=self.request.user)
		permission_classes = [IsOwnerOrReadOnly]

class PostMyListAPIView(ListAPIView):
	serializer_class = PostListSerializer
	permission_classes = [IsAuthenticated]
	def get_queryset(self, *args, **kwargs):
		queryset_list = Post.objects.all().filter(user = self.request.user.id)
		return queryset_list















	

	