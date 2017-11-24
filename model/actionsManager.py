from model import action

class Actions:

    def __init__(self):
        self.ListOfActions = []

    def AddAction(self, Account, module):
        self.ListOfActions.append(action.Action(Account,module))

    def GetAction(self, id):
        return self.ListOfActions[id]