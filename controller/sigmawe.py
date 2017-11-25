
from model import accountManager
from model import actionsManager
from model import modulesManager
from controller.serializer import helperSerializer
import os

class SigmaWE:

    def __init__(self):
        self.sigmaPath= os.path.abspath(__file__).split("sigmaWE")[0] + "sigmaWE\\"
        self.Serializer = helperSerializer(self.sigmaPath)


        ##create acc manager and load data form file if exists
        self.AccManager = accountManager.AccountManager()
        self._loadAllAccounts()

        self.ModuleManager= modulesManager.moduleManager()
        self._loadAllModules()

        self.ActionManager = actionsManager.Actions()

    def GetAllAccounts(self):
        self.AccManager.GetAllAccounts()

    def GetAllActions(self):
        self.ActionManager.GetAllActions()

    def GetAllModules(self):
        self.ModuleManager.GetAllModules()



    def AddSingleAccount(self, email, password, toRemember):
        if(not toRemember):
            self.AccManager.AddAccount(email,password)

        data={}
        ##iterate through accounts find ones with to remember flag and save them into data
        for key in self.AccManager.Accounts:
            if self.AccManager.GetAccount(key).ToRemember:
                data.update({key : self.AccManager.GetAccount(key)})
        self.Serializer.save("Accounts.dat",data)

    def RemoveSingleAccount(self, email):
        self.AccManager.RemoveAccount(email)

    def ActiveBehaviourOnAccount(self, email, moduleName, kwargs):
        self.ActionManager.AddAction(self.AccManager.GetAccount(email), moduleName, kwargs)


    def DeactivateBehaviour(self, email, module):
        self.ActionManager.StopAction(email, module)

    def LoadModule(self,moduleName):
        self.ModuleManager.loadModules([moduleName])



    ##loaders from pickled files
    def _loadAllAccounts(self):
        if (os.path.isfile(self.Serializer.path + "Accounts.dat")):
            self.AccManager.Accounts = self.Serializer.load("Accounts.dat")

    def _loadAllModules(self):
        for behaviour in os.listdir(self.sigmaPath+"\\behaviours"):
            self.ModuleManager.loadModules([behaviour.split(".")[0]])


