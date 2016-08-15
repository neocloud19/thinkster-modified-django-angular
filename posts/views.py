# IMPORTS
from rest_framework import permissions, viewsets
from rest_framework.response import Response

from posts.models import Post
from posts.permissions import IsAuthorOfPost
from posts.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    API:

    """

    # 1. Define the data to be queried
    queryset = Post.objects.order_by('created_at')

    # 2. Define the serializer class to use
    serializer_class = PostSerializer

    def get_permissions(self):
        """

        :return:
        """
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAuthorOfPost())

    def perform_create(self, serializer):
        """

        :param serializer:
        :return:
        """

        # 1. Save the post with the author
        instance = serializer.save(author=self.request.user)

        return super(PostViewSet, self).perform_create(serializer)


class AccountPostViewSet(viewsets.ViewSet):
    """

    """
    # 1. Define the data to be queried
    queryset = Post.objects.select_related('author').all()

    # 2. Define the serializer class to use
    serializer_class = PostSerializer

    def list(self, request, account_username=None):
        """

        :param request:
        :param account_username:
        :return:
        """

        # 1. Define the data to be shown
        queryset = self.queryset.filter(author__username=account_username)

        # 2. Define the serializer class to use
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)






























