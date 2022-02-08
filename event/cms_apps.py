from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class AgendaApphook(CMSApp):
    app_name = "events" # Name used in template
    name = "Agenda Application"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["apps.agenda.event.urls"]


apphook_pool.register(AgendaApphook)  # register your app
