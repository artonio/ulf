from typing import ClassVar

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import os

class DrawerIconChooserDialog(Gtk.FileChooserDialog):
    def __init__(self, parent):
        Gtk.FileChooserDialog.__init__(self, "Choose App Icon", parent,
                                       Gtk.FileChooserAction.OPEN,
                                       (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                        Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        initDir = os.getenv('HOME') + "/Pictures/icons"
        self.set_current_folder(initDir)