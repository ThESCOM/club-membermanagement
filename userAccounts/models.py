from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.utils.translation import ugettext_lazy as _

class AdminUser(AbstractBaseUser):
    email = models.EmailField(_("Email"), unique=True, db_index=True)
    is_Active = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __unicode__(self):
        return self.email
