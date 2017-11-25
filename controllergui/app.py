import tkinter as tk
from controller.sigmawe import SigmaWE
from controllergui.events import EventHandler
from view import masterview as masterV

class App:
    def __init__(self):
        self.dataClient= SigmaWE()
        root = tk.Tk()
        self.viewClient= masterV.MasterView(root, self.dataClient)
        self.viewClient.pack()
        self.eventClient = EventHandler(self.dataClient, self.viewClient)
        self.addBindings()

        root.mainloop()

    def addBindings(self):
        """binds events to event handler"""

        self.viewClient.accountsSuperView.addAccountButton.bind("<ButtonRelease>",self.eventClient.addAccount)


