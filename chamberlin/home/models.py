# Standard Library imports
from __future__ import unicode_literals

# Django Imports
from django.utils import timezone
from django.db import models


# Model to update "Home" without re-writing html
class Home(models.Model):

    class Meta:
        verbose_name_plural = 'Home'

    headline = models.CharField(max_length=40)
    sub_headline = models.CharField(max_length=50)
    call_to_action = models.CharField(max_length=40)
    pub_date = models.DateField(default=timezone.now)


# Model to update "About Me" without re-writing html
class About(models.Model):

    class Meta:
        verbose_name_plural = 'About'

    header = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    bio = models.TextField()
    pub_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.header


class Contact(models.Model):

    class Meta:
        verbose_name_plural = 'Contact'

    title = models.CharField(max_length=30)
    facebook = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    pub_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title
