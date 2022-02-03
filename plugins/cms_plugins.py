from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from .models import AgendaPlugin


class AgendaPlugin(CMSPluginBase):
    model = AgendaPlugin
    name = _("Agenda Plugin")
    render_template = "agenda.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(AgendaPlugin)