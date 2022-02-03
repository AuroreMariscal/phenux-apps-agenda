from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class EventApp(CMSApp):
    app_name = "events"
    name = "Event App"
    urls = ["apps.agenda.event.urls"]


apphook_pool.register(EventApp)  # register your app
