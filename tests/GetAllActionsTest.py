from model import actionsManager
from model import accountManager
from model import modulesManager
from model import account

firstAccount = account.Account("dddf@koszmail.pl", "przemekssie")
secondAccount = account.Account("email1", "haslo1")



am = actionsManager.Actions()


modulesMan= modulesManager.moduleManager()
modulesMan.loadModules(["hydra"])
hydrModule= modulesMan.getModule("hydra")





am.AddAction(firstAccount,hydrModule,{"CONFID":"1668412989883731"})

test = am.GetAllActionsRunnedOnAccount("dddf@koszmail.pl")
input("s")