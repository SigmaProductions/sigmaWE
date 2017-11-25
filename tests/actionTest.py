from model.action import Action
from model.account import Account
from model import modulesManager

login=
password=

modulesMan= modulesManager.moduleManager()
modulesMan.loadModules(["hydra"])
hydrModule= modulesMan.getModule("hydra")

act=Action(Account(login,password,True),hydrModule,{"CONFID":"1168310503269787"})
act.Run()
input("s")