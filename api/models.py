from django.db import models
from django.utils.translation import gettext_lazy as _


class SiteData(models.Model):
    category = models.CharField(max_length=255, unique=True, error_messages={
        'unique': _("This category already exist.")
    })
    data = models.JSONField(null=True, blank=True)


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True, error_messages={
        'unique': _("A user with that email already exists."),
    })


class Message(models.Model):
    email = models.EmailField(blank=True, null=True)
    name = models.CharField(max_length=255)
    message = models.TextField()
