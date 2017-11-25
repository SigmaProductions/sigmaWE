
class EventHandler:
    def __init__(self,dataController, masterView):
        self.dataClient = dataController
        self.viewClient = masterView

    def addAccount(self, event):
        self.viewClient.accountsSuperView.spawnAddAccountWindow()
        print("test")

    def okAddAccount(self,email,password,save):
        self.dataClient.AddSingleAccount(email,password,save)
        self.viewClient.accountsSuperView.showAccounts()