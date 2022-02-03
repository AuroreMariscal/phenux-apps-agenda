from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from cms.utils.urlutils import admin_reverse
from cms.cms_toolbars import PAGE_MENU_IDENTIFIER
from django.utils.translation import ugettext_lazy as _


class EventToolbar(CMSToolbar):

    def populate(self):
        page_menu = self.toolbar.get_menu(PAGE_MENU_IDENTIFIER)
        if page_menu:
            page_menu.add_break(identifier='agenda_section')

            agenda_menu = page_menu.get_or_create_menu(
                key='agenda',
                verbose_name='Agenda'
            )

            agenda_menu.add_modal_item(
                _('Add event'),
                url=admin_reverse('event_event_add')
            )


# register the toolbar
toolbar_pool.register(EventToolbar)
