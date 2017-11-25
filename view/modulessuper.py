import tkinter as tk
from view import accaddwindow


class ModulesSuperview(tk.Frame):
    def __init__(self,master, modules):
        super().__init__(master)
        self.modulesManager=modules
        self.accountListBox= tk.Listbox(self)
        self.accountListBox.pack()

        self._showModules()

    def _showModules(self):
        self.accountListBox.delete(0,tk.END)
        if(self.modulesManager.modules==None):
            return
        for key in self.modulesManager.GetAllModules():
            self.accountListBox.insert(tk.END, key)


