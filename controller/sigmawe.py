from helper.readUsersFromFile import readUsersFromFile
from model import accountManager as am
from model import actionsManager as actionM


class SigmaWE:

    def __init__(self):
        self.AccManager = am.AccountManager()
        self.ModuleManager=None
        self.ActionManager = actionM.Actions()


    def AddAcountsFromFile(self):
        users = readUsersFromFile()
        self.AccManager.AddMultipleAccounts(users)

    def AddSingleAccount(self, email, password):
        self.AccManager.AddAccount(email,password)

    def RemoveSingleAccount(self, email):
        self.AccManager.RemoveAccount(email)

    def ActiveBehaviourOnAccount(self, email, moduleName, kwargs):
        self.ActionManager.AddAction(self.AccManager.GetAccount(email), moduleName, kwargs)

    def GetAllAccounts(self):
        self.AccManager.GetAllAccounts()

    #def GetAllModules(self):
       # self.ModuleManager.g

    #load all modules

    def LoadModule(self,moduleName):
        self.ModuleManager.loadModules([moduleName])
