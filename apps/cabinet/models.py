from os import path, remove

from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver

from apps.commons.utils.models import BaseDbItem


class UserFile(BaseDbItem):
    def upload_path(self, filename):
        return 'uploads/{0}/{1}'.format(self.user.id, filename)

    upload = models.FileField(upload_to=upload_path)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, blank=True)


@receiver(models.signals.post_delete, sender=UserFile)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `UserFile` object is deleted.
    """
    if instance.upload:
        if path.isfile(instance.upload.path):
            remove(instance.upload.path)