# IMPORTS
from rest_framework import permissions


class IsAuthorOfPost(permissions.BasePermission):
    """

    """

    def has_object_permission(self, request, view, post):
        """

        :param request:
        :param view:
        :param obj:
        :return:
        """
        if request.user:
            return post.author == request.user

        return False