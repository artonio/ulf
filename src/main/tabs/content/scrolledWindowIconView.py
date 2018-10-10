import gi

from src.main.tabs.content.shortcutsIconView import ShortcutsView

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from typing import ClassVar

class ScrolledWindowIconView(Gtk.ScrolledWindow):

    is_new_file: ClassVar[bool]
    drawer_name: ClassVar[str]
    drawer_icon_file_name: ClassVar[str]

    icon_view: ShortcutsView = ShortcutsView()

    def __init__(self, targets, drawer_name: str, drawer_icon_file_name: str, is_new_file: bool):
        Gtk.ScrolledWindow.__init__(self)
        self.is_new_file = is_new_file
        self.drawer_name = drawer_name
        self.drawer_icon_file_name = drawer_icon_file_name

        self.set_min_content_height(200)
        self.set_min_content_width(400)

        self.set_border_width(0)
        self.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.ALWAYS)

        self.icon_view.drag_dest_set_target_list(targets)
