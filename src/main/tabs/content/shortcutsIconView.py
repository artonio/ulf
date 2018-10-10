import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from typing import ClassVar, Dict, List

class ShortcutsView(Gtk.IconView):

    drawerSettings: ClassVar[Dict[str, str]] = {}
    launchDict: ClassVar[Dict[str, str]] = {}
    iconFileNamesList: ClassVar[List[str]] = []

    def __init__(self):
        Gtk.IconView.__init__(self)