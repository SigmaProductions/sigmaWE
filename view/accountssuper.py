import tkinter as tk
from view import accaddwindow
class AccountsSuperview(tk.Frame):
    def __init__(self,master):
        super().__init__(master)

        self.accountListBox= tk.Listbox(self)
        self.accountListBox.insert(1,"adsfas")
        self.accountListBox.insert(2, "adsfas")
        self.accountListBox.grid(column=0, rowspan=2)

        self.addAccountButton= tk.Button(self,text="Add")
        self.addAccountButton.grid(column=1, row=0,pady=2, padx=5, sticky=tk.W+tk.E+tk.S)

        self.removeAccountButton = tk.Button(self, text="Remove")
        self.removeAccountButton.grid(column=1, row=1,pady=2,padx=5,sticky= tk.N)

        self.callbackAddWindow=None


    def spawnAddAccountWindow(self):
        AddAccountWindowRoot = tk.Toplevel(self)
        self.AddAccountWnd = accaddwindow.AccountAddWindow(AddAccountWindowRoot)
        self.AddAccountWnd.pack()
        self.AddAccountWnd.OkButtonCallback=self.callbackAddWindow
    def addBindingToAccWndOK(self,callback):
        self.callbackAddWindow=callback
