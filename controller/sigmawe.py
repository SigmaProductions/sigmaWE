from helper.readUsersFromFile import readUsersFromFile
from model import accountManager as am
from model import actionsManager as actionM


class SigmaWE:

    def __init__(self):
        self.AccManager = am.AccountManager()
        self.ModuleManager=None
        self.ActionManager = actionM.Actions()

    def GetAllAccounts(self):
        self.AccManager.GetAllAccounts()

    def GetAllActions(self):
        self.ActionManager.GetAllActions()

    def GetAllModules(self):
        self.ModuleManager.GetAllModules()

    def AddAcountsFromFile(self):
        users = readUsersFromFile()
        self.AccManager.AddMultipleAccounts(users)

    def AddSingleAccount(self, email, password, toRemember):
        self.AccManager.AddAccount(email,password, toRemember)

    def RemoveSingleAccount(self, email):
        self.AccManager.RemoveAccount(email)

    def ActiveBehaviourOnAccount(self, email, moduleName, kwargs):
        self.ActionManager.AddAction(self.AccManager.GetAccount(email), moduleName, kwargs)
    #load all modules

    def DeactivateBehaviour(self, email, module):
        self.ActionManager.StopAction(email, module)

    def LoadModule(self,moduleName):
        self.ModuleManager.loadModules([moduleName])
