from rest_framework.serializers import (ModelSerializer,
                                        HyperlinkedIdentityField,
                                        SerializerMethodField
                                        )
from apps.posts.models import Post
from apps.accounts.api.serializers import UserDetailSerializer



post_detail_url = HyperlinkedIdentityField(view_name='posts-api:detail',lookup_field='slug')

class PostListSerializer(ModelSerializer):
    url = post_detail_url
    author =  UserDetailSerializer(read_only =True)
    class Meta:
        model = Post
        fields = [
            'url',
            'author',
            'title',
            'text',
            'published_date',
        ]




class PostDetailSerializer(ModelSerializer):
    url = post_detail_url
    author = UserDetailSerializer(read_only =True)
    image = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'url',
            'id',
            'author',
            'title',
            'slug',
            'text',
            'published_date',
            'image',
        ]

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            # 'id',
            'title',
            # 'slug',
            'text',
            'published_date',
        ]
