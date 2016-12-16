from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UploadDocument(models.Model):
    def __init__(self, user):
        super(models.Model, self)
        self.user = user
        path = user.fist_name + '_' + user.last_name + '/%Y/%m/%d'
        self.document = models.FileField(upload_to= path)
