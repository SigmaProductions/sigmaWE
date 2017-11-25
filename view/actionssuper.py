import tkinter as tk


class ActionsSuperview(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.engageButton= tk.Button(self,text="Engage",bg="red")
        self.engageButton.pack(side="left",fill=tk.Y)#grid(column=0,row=0, rowspan=2,sticky=tk.N+tk.S+tk.E+tk.W)

        self.actionsList= tk.Listbox(self)
        self.actionsList.pack(side="left",fill=tk.Y)#grid(column=1,row=0,rowspan=2)
        """""""""
        self._showModules()

        def _showModules(self):
        self.accountListBox.delete(0,tk.END)
        if(self.modulesManager.modules==None):
            return
        for key in self.modulesManager.GetAllModules():
            self.accountListBox.insert(tk.END, key)
        """""""""


