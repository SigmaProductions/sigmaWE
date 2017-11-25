from model import actionsManager

from model import accountManager as am
from model import account
from model import accountManager


accm = accountManager.AccountManager()
accm.AddAccount("dddf@koszmail.pl", "przemekssie", True)
accm.AddAccount("email1", "haslo1", False)
test = accm._GetAccountsToRemember()
input('s')