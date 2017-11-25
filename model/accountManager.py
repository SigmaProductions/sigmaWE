from model import account

class AccountManager:

    def __init__(self):
        self.Accounts = {}

    def AddAccount(self, email, password):
        accountToAdd = account.Account(email, password)
        tempDict = {accountToAdd.Email: accountToAdd}
        self.Accounts.update(tempDict)

    def RemoveAccount(self, email):
        self.Accounts.pop(email)

    def GetAccount(self, email):
        return self.Accounts[email]

    def GetAllAccounts(self):
        return self.Accounts

    def AddMultipleAccounts(self, AccountsToLoad):
        for key, value in AccountsToLoad.items():
            self.AddAccount(key, value)



