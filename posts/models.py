# IMPORTS
from django.db import models
from authentication.models import Account


class Post(models.Model):
    """
    POST
    """

    # ATTRIBUTES
    author = models.ForeignKey(Account)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # METHODS

    def __unicode__(self):
        """
        Return data when ask for the string form

        :return:
        """
        return '{0}'.format(self.content)