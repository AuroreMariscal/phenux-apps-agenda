from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from .urls import urlpatterns


class AgendaApphook(CMSApp):
    app_name = "events" # Name used in template
    name = "Agenda Application"

    def get_urls(self, page=None, language=None, **kwargs):
        return urlpatterns


apphook_pool.register(AgendaApphook)  # register your app
