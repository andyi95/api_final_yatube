from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Post, Comment, Follow, User, Group


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Post

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', )
        model = Group

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment

class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),  # Как вариант get_user_mode().objects.all()
        slug_field='username'
    )
    class Meta:
        fields = '__all__'
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            )
        ]
    # following = serializers.SlugField(
    #     source='following.username',
    #     required=True
    # )
    # user = serializers.ReadOnlyField(
    #     source='user.username',
    #     default=serializers.CurrentUserDefault()
    # )

    # class Meta:
    #     fields = ('id', 'user', 'following')
    #     model = Follow