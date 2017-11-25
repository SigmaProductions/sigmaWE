from model import action

class Actions:

    def __init__(self):
        self.ListOfActions = []

    def AddAction(self, Account , module, kwargs):
        ##account is of account class and module is imported module from module maanger, kwargs is dict of parameters
        ActionToActivate = action.Action(Account,module,kwargs)
        self.ListOfActions.append(ActionToActivate)
        ActionToActivate.Run()

    def GetAction(self, id):
        return self.ListOfActions[id]

    def GetAllActionsRunnedOnAccount(self, email):
        acctionsToReturn = []
        for index, member in enumerate(self.ListOfActions):
            if(member.AccPtr.Email == email):
                acctionsToReturn.append(member)


        return acctionsToReturn

    def GetAllActions(self):
        return self.ListOfActions

