from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
import os
import binascii


class Token(models.Model):
    key = models.CharField(_("key"), max_length=40, primary_key = True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name = 'auth_token',
        on_delete=models.CASCADE, verbose_name = _("User")
    )
    created = models.DateTimeField(_("Created"), auto_now_add=True)


class Post(models.Model):
    title = models.CharField(max_length=200)
    content =models.TextField()\
        
        
    def __str__(self):
        return self.title
    