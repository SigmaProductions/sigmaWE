import tkinter as tk
import view.accountssuper as accSuperview
class MasterView(tk.Frame):
    def __init__(self,master, dataController):
        super().__init__(master)

        self.dataClient= dataController

        self.accountsSuperView= accSuperview.AccountsSuperview(self)
        self.accountsSuperView.pack()
