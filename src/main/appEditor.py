import gi

from src.main.dialogs.newDrawerDialog import NewDrawerDialog
from src.main.tabs.tabsView import Tabs

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from typing import ClassVar


class MainWindow(Gtk.Window):

    toolbar: ClassVar[Gtk.Toolbar]
    notebook: ClassVar[Tabs]

    def __init__(self):
        Gtk.Window.__init__(self, title="LauncherFolders Editor")
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_decorated(True)
        self.set_opacity(0.9)

        self.toolbar = self.createToolbar()
        self.notebook = Tabs(self)
        self.notebook.createPage('Test', '', False)

        hbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)

        hbox.pack_start(self.toolbar, True, True, 0)
        hbox.pack_end(self.notebook, True, True, 0)
        self.add(hbox)

    def createToolbar(self) -> Gtk.Toolbar:
        toolbar: Gtk.Toolbar = Gtk.Toolbar()

        toolbar.set_style(Gtk.ToolbarStyle.ICONS)

        newDrawerBtn = Gtk.ToolButton()
        newDrawerBtn.set_icon_name("document-new")
        newDrawerBtn.set_tooltip_text("New Drawer")
        newDrawerBtn.connect("clicked", self.newDrawerClicked)

        openDrawerBtn = Gtk.ToolButton.new()
        openDrawerBtn.set_icon_name("document-open")
        openDrawerBtn.set_tooltip_text("Open Drawer")
        # openDrawerBtn.connect("clicked", self.openDrawerClicked)

        saveDrawerBtn = Gtk.ToolButton.new()
        saveDrawerBtn.set_icon_name("document-save")
        saveDrawerBtn.set_tooltip_text("Save Drawer and add to launcher")
        # saveDrawerBtn.connect("clicked", self.saveDrawerClicked)

        drawerPreferencesBtn = Gtk.ToolButton.new()
        drawerPreferencesBtn.set_icon_name("gtk-preferences")
        drawerPreferencesBtn.set_tooltip_text("Drawer Settings")
        # drawerPreferencesBtn.connect("clicked", self.drawerPreferencesClicked)

        drawerPreviewBtn = Gtk.ToolButton.new()
        drawerPreviewBtn.set_icon_name("media-playback-start")
        drawerPreviewBtn.set_tooltip_text("Preview Drawer")
        # drawerPreviewBtn.connect("clicked", self.drawerPreviewClicked)

        toolbar.insert(newDrawerBtn, -1)
        toolbar.insert(openDrawerBtn, -1)
        toolbar.insert(saveDrawerBtn, -1)
        toolbar.insert(Gtk.SeparatorToolItem.new(), -1)
        toolbar.insert(drawerPreferencesBtn, -1)
        toolbar.insert(drawerPreviewBtn, -1)

        return toolbar

    def newDrawerClicked(self, widget):
        new_drawer_dialog: NewDrawerDialog = NewDrawerDialog(self)

        response = new_drawer_dialog.run()

        if response == Gtk.ResponseType.OK:
            drawer_name = new_drawer_dialog.drawer_name.get_text()
            drawer_icon = new_drawer_dialog.drawer_icon_file_name

            if not drawer_name:
                print("Enter Drawer Name")
            else:
                self.notebook.createPage(drawer_name, drawer_icon, True)
            print("ok")
        elif response == Gtk.ResponseType.CANCEL:
            print("cancel")
        new_drawer_dialog.destroy()



window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()