from model import action

class Actions:

    def __init__(self):
        self.ListOfActions = []

    def AddAction(self, Account , module, kwargs):
        ##account is of account class and module is imported module from module maanger, kwargs is dict of parameters
        self.ListOfActions.append(action.Action(Account,module,kwargs))

    def GetAction(self, id):
        return self.ListOfActions[id]