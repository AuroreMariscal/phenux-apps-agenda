from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from django.db import models


class AgendaPluginModel(CMSPlugin):
    title = models.CharField(max_length=50, default='Title')