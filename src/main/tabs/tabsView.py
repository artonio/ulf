from typing import ClassVar

import gi

from src.main.tabs.content.scrolledWindowIconView import ScrolledWindowIconView
from src.main.tabs.tabLabel import TabLabel

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

(URI_LIST_MIME_TYPE, TEXT_LIST_MIME_TYPE) = range(2)

class Tabs(Gtk.Notebook):
    parent: ClassVar[Gtk.Window]
    targets: ClassVar[Gtk.TargetList]

    def __init__(self, parentWindow: Gtk.Window):
        Gtk.Notebook.__init__(self)
        self.parent = parentWindow
        self.targets = Gtk.TargetList.new([])
        self.targets.add_uri_targets(URI_LIST_MIME_TYPE)
        self.targets.add_text_targets(TEXT_LIST_MIME_TYPE)

    def createPage(self, drawer_label: str, drawer_icon_file_name: str, isNewFile: bool):
        scrolled_window = self.createContent(drawer_label, drawer_icon_file_name, isNewFile)

        tab_label: TabLabel = TabLabel(drawer_label, drawer_icon_file_name)
        tab_label.connect("close-clicked", self.on_close_clicked, self, scrolled_window)

        self.append_page(scrolled_window, tab_label)
        self.show_all()

    def on_close_clicked(self, tab_label, notebook, tab_widget):
        self.remove_page(notebook.page_num(tab_widget))

    def createContent(self, drawer_label, drawer_icon_file_name, is_new_file):
        return ScrolledWindowIconView(self.targets, drawer_label, drawer_icon_file_name, is_new_file)


