from rest_framework import serializers
from blog_app.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'slug', 'content', 'category', 'author', 'publishes', 'created_at')
        read_only_fields = ('id', 'publishes', 'created_at', 'author', 'slug')
