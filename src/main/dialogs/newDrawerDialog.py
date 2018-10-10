from typing import ClassVar

import gi

from src.main.dialogs.drawerIconChooserDialog import DrawerIconChooserDialog

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf


class NewDrawerDialog(Gtk.Dialog):

    drawer_icon_file_name: ClassVar[str] = ""
    drawer_name: ClassVar[Gtk.Entry]
    drawer_icon: ClassVar[Gtk.Button]

    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "New Drawer", parent, 0,
                            (Gtk.STOCK_CANCEL,
                             Gtk.ResponseType.CANCEL,
                             Gtk.STOCK_OK,
                             Gtk.ResponseType.OK))

        box: Gtk.Box = self.get_content_area()

        # dImage = "gtk-page-setup"
        # dImage = "gtk-missing-image"
        dImage = "gtk-select-color"

        self.drawer_name = Gtk.Entry()
        self.drawer_icon = Gtk.Button.new_from_icon_name(dImage, 4)
        self.drawer_icon.connect("clicked", self.on_new_drawer_icon_click)

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        hbox.pack_start(self.drawer_name, False, True, 0)
        hbox.pack_end(self.drawer_icon, True, True, 0)

        box.add(hbox)
        self.show_all()

    def on_new_drawer_icon_click(self, widget):
        dialog = DrawerIconChooserDialog(self)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            self.drawer_icon_file_name = dialog.get_filename()
            self.drawer_icon.set_image(Gtk.Image.new_from_pixbuf(self.getPixBuffFromFile(self.drawer_icon_file_name)))
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")
        dialog.destroy()

    def getPixBuffFromFile(self, fileName) -> GdkPixbuf.Pixbuf:
        pixbuf: GdkPixbuf.Pixbuf = GdkPixbuf.Pixbuf.new_from_file(fileName)
        pixbuf = pixbuf.scale_simple(48, 48, GdkPixbuf.InterpType.BILINEAR)

        return pixbuf

