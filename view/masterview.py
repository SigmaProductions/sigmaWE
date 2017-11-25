import tkinter as tk
import os
import view.accountssuper as accSuperview
import view.modulessuper as modulesSuperview
import view.actionssuper as actionsSuperview
class MasterView(tk.Frame):
    def __init__(self,master, dataController):
        super().__init__(master)
        self.master.title("SigmaWE")
        self.master.iconbitmap(os.path.abspath(__file__).split("sigmaWE")[0] + "sigmaWE\\view\\BoS_logo.ico")
        self.dataClient= dataController

        self.accountsSuperView= accSuperview.AccountsSuperview(self,self.dataClient)
        self.accountsSuperView.grid(column=0,row=0)

        self.modulesSuperView= modulesSuperview.ModulesSuperview(self,self.dataClient.ModuleManager)
        self.modulesSuperView.grid(column=0,row=1,sticky=tk.W, pady=20)

        self.actionsSuperView= actionsSuperview.ActionsSuperview(self)
        self.actionsSuperView.grid(column=1, row=0,rowspan=2,columnspan=5,sticky=tk.N+tk.S)
