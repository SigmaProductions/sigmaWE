from model import account

class AccountManager:

    def __init__(self):
        self.Accounts = {}

    def AddAccount(self, email, password, toRemember):
        accountToAdd = account.Account(email, password, toRemember)
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

    def _GetAccountsToRemember(self):
        accountsToRemember = []
        for key, value in self.Accounts.items():
            if(value.ToRemember == True):
                accountsToRemember.append(value)


        return accountsToRemember


