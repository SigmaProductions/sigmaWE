from helper.readUsersFromFile import readUsersFromFile
from model import accountManager as am


class SigmaWE:

    def __init__(self):
        self.accManager = am.AccountManager()
        self.ModuleManager=None

    def addAcountsFromFile(self):
        users = readUsersFromFile()
        self.accManager.AddMultipleAccounts(users)

