from model import actionsManager

from model import modulesManager
from model import account

firstAccount = account.Account("dddf@koszmail.pl", "przemekssie")
secondAccount = account.Account("email1", "haslo1")

am = actionsManager.Actions()

modulesMan= modulesManager.moduleManager()
modulesMan.loadModules(["hydra"])
hydrModule= modulesMan.getModule("hydra")

modulesMan.loadModules(["autoBirths"])
birthModule=modulesMan.getModule("autoBirths")


am.AddAction(firstAccount, hydrModule,{"CONFID":"1668412989883731"})
am.AddAction(firstAccount, birthModule, {})

test = am.GetAllActionsRunnedOnAccount("dddf@koszmail.pl")
input("s")