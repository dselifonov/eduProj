from django.contrib.auth.models import User
from django.db import models


class BaseDbItem(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='%(class)s_created_by')
    modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='%(class)s_modified_by')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
