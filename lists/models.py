from django.shortcuts import resolve_url
from django.db import models

class List(models.Model):

    def get_absolute_url(self):
        return resolve_url('view_list', self.id)

    pass

class Item(models.Model):
    text = models.TextField()
    list = models.ForeignKey(List)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
