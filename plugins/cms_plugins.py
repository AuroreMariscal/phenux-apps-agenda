from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from .models import AgendaPluginModel
from apps.agenda.event.models import Event


class AgendaPluginPublisher(CMSPluginBase):
    model = AgendaPluginModel
    name = _("Agenda")
    module = _("Agenda")
    render_template = "agenda.html"
    cache = False

    def render(self, context, instance, placeholder):
        list = Event.objects.all()
        context.update({
            'list': list,
            'instance': instance,
        })
        return context

plugin_pool.register_plugin(AgendaPluginPublisher)