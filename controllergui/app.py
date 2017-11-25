import tkinter as tk
from controller.sigmawe import SigmaWE

from view import masterview as masterV

class App:
    def __init__(self):
        self.dataClient= SigmaWE()
        self.root = tk.Tk()

        self.viewClient= masterV.MasterView(self.root, self.dataClient)
        self.viewClient.pack()

        self.root.mainloop()

    def addBindings(self):
        """binds events to event handler"""


