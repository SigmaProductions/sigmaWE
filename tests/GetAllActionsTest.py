from model import actionsManager
from model import accountManager
from model import modulesManager
from model import account

firstAccount = account.Account("dddf@koszmail.pl", "przemekssie")
secondAccount = account.Account("email1", "haslo1")



am = actionsManager.Actions()


modulesMan= modulesManager.moduleManager()
modulesMan.loadModules(["mention"])
hydrModule= modulesMan.getModule("mention")





am.AddAction(firstAccount,hydrModule,{"CONFID":"1168310503269787"})

test = am.GetAllActionsRunnedOnAccount("dddf@koszmail.pl")
input("s")