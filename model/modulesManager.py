import importlib

class moduleManager:
    def __init__(self):
        self.modules=dict()

    def loadModules(self,moduleNames):
        for singleModuleName in moduleNames:
            self.modules.update({singleModuleName : importlib.import_module("behaviours."+singleModuleName)})

    def getModule(self,moduleName):
        return self.modules[moduleName]

    def GetAllModules(self):
        return self.modules