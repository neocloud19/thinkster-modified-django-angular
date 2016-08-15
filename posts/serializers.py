# IMPORTS
from rest_framework import serializers
from authentication.serializers import AccountSerializer
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer
    """

    # 1. Get the author of the post as read only
    author = AccountSerializer(read_only=True, required=False)

    class Meta:
        """
        Define which data will be serialized
        """

        # 2. Declare the serializing data
        model = Post

        # 3. Declare the available fields from the data
        fields = ('id', 'author', 'content', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def get_validation_exclusions(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """

        exclusions = super(PostSerializer, self).get_validation_exclusions()

        return exclusions + ['author']



