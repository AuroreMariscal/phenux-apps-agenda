from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _


class Event(models.Model):
    title = models.CharField(max_length=30, blank=False)

    url = models.CharField(max_length=20, unique=True, blank=False)

    description = models.CharField(max_length=200, blank=True)

    featured_image = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=100)

    publishing_date = models.DateTimeField(_('publishing date'),
                                           default=now)

    is_published = models.BooleanField(_('is published'), default=False,
                                       db_index=True)

    is_featured = models.BooleanField(_('is featured'), default=False,
                                      db_index=True)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'List of events'