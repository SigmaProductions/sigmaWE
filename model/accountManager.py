from model import account

class AccountManager:

    def __init__(self):
        self.Accounts = {}

    def AddAccount(self, email, password):
        accountToAdd = account.Account(email, password)
        tempDict = {accountToAdd.email: accountToAdd}
        self.Accounts.update(tempDict)





