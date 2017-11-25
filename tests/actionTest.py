from model.action import Action
from model.account import Account
from model import modulesManager

login=
password=

modulesMan= modulesManager.moduleManager()
modulesMan.loadModules(["hydra"])
hydrModule= modulesMan.getModule("hydra")

act=Action(Account(login,password),hydrModule,{"CONFID":"1668412989883731"})
act.Run()
input("s")