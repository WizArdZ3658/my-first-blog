from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
from blog.models import Post


class PostListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name='detail')
    del_url = HyperlinkedIdentityField(view_name='delete')
    author = SerializerMethodField()

    class Meta:
        model = Post
        fields = ['url', 'author', 'title', 'text', 'likes', 'published_date', 'del_url']

    def get_author(self, obj):
        return str(obj.author.username)


class PostDetailSerializer(ModelSerializer):
    author = SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'text', 'likes', 'published_date', 'created_date']

    def get_author(self, obj):
        return str(obj.author.username)


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'text']
