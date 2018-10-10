import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango, GdkPixbuf
from typing import ClassVar, Dict, List

UI_INFO = """
<ui>
  <popup name='PopupMenu'>
    <menuitem action='Properties' />
    <separator />
    <menuitem action='DeleteItem' />
  </popup>
</ui>
"""

(COLUMN_TEXT, COLUMN_PIXBUF) = range(2)

class ShortcutsView(Gtk.IconView):

    drawerSettings: ClassVar[Dict[str, str]] = {}
    launchDict: ClassVar[Dict[str, str]] = {}
    iconFileNamesList: ClassVar[List[str]] = []
    uimanager: ClassVar[Gtk.UIManager]

    def __init__(self):
        Gtk.IconView.__init__(self)

        action_group = Gtk.ActionGroup("right_click_actions")

        action_deleteItem = Gtk.Action("DeleteItem", "Delete", None, None)
        # action_deleteItem.connect("activate", self.on_delete_item)
        action_group.add_action(action_deleteItem)

        action_properties = Gtk.Action("Properties", "Properties", None, None)
        # action_properties.connect("activate", self.on_item_properties)
        action_group.add_action(action_properties)

        self.uimanager = Gtk.UIManager()
        self.uimanager.insert_action_group(action_group)
        self.uimanager.add_ui_from_string(UI_INFO)
        self.popup = self.uimanager.get_widget("/PopupMenu")

        self.set_item_padding(0)
        # self.set_item_width(self.iconSize)
        self.set_columns(4)
        self.set_column_spacing(0)
        self.set_selection_mode(Gtk.SelectionMode.SINGLE)
        self.props.activate_on_single_click = False

        self.model = Gtk.ListStore(str, GdkPixbuf.Pixbuf)
        self.set_model(self.model)

        self.set_text_column(COLUMN_TEXT)
        self.set_pixbuf_column(COLUMN_PIXBUF)

    def set_font(self):
        fontO = Pango.FontDescription("Ubuntu " + str(self.fontSize))
        self.modify_font(fontO)