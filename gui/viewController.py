from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import ListItemButton, ListView


class ViewController(GridLayout):
    def __init__(self, **kwargs):
        super(ViewController, self).__init__(**kwargs)
        self.cols = 6
        self.rows = 6
        self.addUserButton = Button(text="Add user")
        self.removeUserButton = Button(text="Remove user")
        self.addModuleButton = Button(text="Add module")
        self.removeModuleButton = Button(text="Remove module")

        self.add_widget(self.addUserButton)
        self.add_widget(self.removeUserButton)
        self.add_widget(self.addModuleButton)
        self.add_widget(self.removeModuleButton)

        self.data = [{'text': str(i), 'is_selected': False} for i in range(100)]

        self.args_converter = lambda row_index, rec: {'text': rec['text'],
                                                 'size_hint_y': None,
                                                 'height': 25}

        self.list_adapter = ListAdapter(data=self.data,
                                   args_converter=self.args_converter,
                                   cls=ListItemButton,
                                   selection_mode='single',
                                   allow_empty_selection=False)


        self.list_view = ListView(adapter=self.list_adapter)

        self.add_widget(self.list_view)

    def setAddUser(self, callback):
        self.addUserButton.bind(on_press=callback)

    def setRemoveUser(self, callback):
        self.removeUserButton.bind(on_press=callback)

    def setAddModule(self, callback):
        self.addModuleButton.bind(on_press=callback)

    def setRemoveModule(self, callback):
        self.removeModuleButton.bind(on_press=callback)




class MainApp(App):
    viewLayout = None
    def createView(self):
        self.viewLayout = ViewController()
    def build(self):
        return self.viewLayout