from model.action import Action
from model.account import Account
from model import modulesManager

login=
password=

modulesMan= modulesManager.moduleManager()
modulesMan.loadModules(["mention"])
hydrModule= modulesMan.getModule("mention")

act=Action(Account(login,password, True),hydrModule,{"CONFID":"1062960053826912"})
act.Run()
input("s")