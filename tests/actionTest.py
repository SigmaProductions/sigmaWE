from model.action import Action
from model.account import Account
from model import modules

modulesMan= modules.moduleManager()
modulesMan.loadModules(["hydra"])
hydrModule= modulesMan.getModule("hydra")

act=Action(Account("dd","ff"),hydrModule)
act.Run()
input("s")