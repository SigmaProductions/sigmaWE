import tkinter as tk
class AccountAddWindow(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.root=master
        self.save = tk.IntVar()
        self.Label = tk.Label(self,text="Give login info", )
        self.EntryEmail= tk.Entry(self)
        self.EntryPassword= tk.Entry(self)
        self.SaveCheckbox = tk.Checkbutton(self, text="Save login info",variable=self.save)

        self.ButtonsContainer= tk.Frame(self)
        self.OkButton = tk.Button(self.ButtonsContainer, text="Ok", command=self.pinTextToEvent)
        self.CancelButton = tk.Button(self.ButtonsContainer, text="Cancel",command=self.cancelButton)

        self.Label.pack(padx="10",pady="5")
        self.EntryEmail.pack(padx="10",pady="5")
        self.EntryPassword.pack(padx="10",pady="10")
        self.SaveCheckbox.pack()
        self.OkButton.grid(row=0,column=0)
        self.CancelButton.grid(row=0,column=1)
        self.ButtonsContainer.pack()

        self.OkButtonCallback=None


    def pinTextToEvent(self):
        self.OkButtonCallback(self.EntryEmail.get(),self.EntryPassword.get(),self.save.get())
    def cancelButton(self):
            self.root.destroy()