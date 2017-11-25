from helper.readUsersFromFile import readUsersFromFile
from model import accountManager as am
from model import actionsManager as actionM
from gui.viewController import MainApp
from gui.viewController import ViewController


class SigmaWE:

    def __init__(self):
        self.AccManager = am.AccountManager()
        self.ModuleManager = None
        self.ActionManager = actionM.Actions()
        self.emailArray = []

        self.root = MainApp()
        self.root.createView()
        self.viewController = self.root.viewLayout
        self.viewController.setAddUser(self.AddSingleAccount)
        self.viewController.setRemoveUser(self.RemoveSingleAccount)
        self.viewController.setAddModule(self.AddModule)
        self.viewController.setRemoveModule(self.RemoveModule)

        self.root.build()
        self.root.run()




    def AddAcountsFromFile(self):
        users = readUsersFromFile()
        self.AccManager.AddMultipleAccounts(users)

    def AddSingleAccount(self, email, password):
        self.AccManager.AddAccount(email, password)
        self.GetAllAccounts()

    def RemoveSingleAccount(self, email):
        self.AccManager.RemoveAccount(email)
        self.GetAllAccounts()

    def AddModule(self, moduleName):
        print("Add module")
        #self.GetAllModules()

    def RemoveModule(self, moduleName):
        print("Remove module")
        # self.GetAllModules()

    def ActiveBehaviourOnAccount(self, email, moduleName, kwargs):
        self.ActionManager.AddAction(self.AccManager.GetAccount(email), moduleName, kwargs)

    def GetAllAccounts(self):
        self.emailArray = self.AccManager.GetAllAccounts()

    #def GetAllModules(self):
       # self.ModuleManager.g

    #load all modules

    def LoadModule(self,moduleName):
        self.ModuleManager.loadModules([moduleName])


SigmaWE()