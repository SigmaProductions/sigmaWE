from model.action import Action
from model.account import Account
from model import modulesManager

login='b'
password='c'

modulesMan= modulesManager.moduleManager()
modulesMan.loadModules(["mention"])
hydrModule= modulesMan.getModule("mention")


act=Action(Account(login,password,True),hydrModule,{"CONFID":"1168310503269787"})

act.Run()
input("s")