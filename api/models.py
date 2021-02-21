from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
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


class Work(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField(blank=True, null=True)
    rating = models.IntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    image = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
