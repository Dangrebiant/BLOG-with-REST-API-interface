from rest_framework.serializers import ModelSerializer

from posts.models import Post
from accounts.api.serializers import UserDetailSerializer


class PostCreateSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
			#'id',
			'title',
			#'slug',
			'content',
			'timestamp',
			#'user'
		]

class PostDetailSerializer(ModelSerializer):
	user = UserDetailSerializer(read_only = True)
	class Meta:
		model = Post
		fields = [
			'id',
			'title',
			'slug',
			'content',
			'timestamp',
			'user'
		]

class PostListSerializer(ModelSerializer):
	user = UserDetailSerializer(read_only = True)
	class Meta:
		model = Post
		fields = [
			'id',
			'title',
			'slug',
			'content',
			'timestamp',
			'user'
		]




#'''

#data = {
#	"title":"Some title",
#	"content":"New content",
#	"timestamp":"2016-07-12"
#}

#new_item = PostSerializer(data = data)
#if new_item.is_valid():
#	new_item.save()
#else:
#	print(new_item.errors)

