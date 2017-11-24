import threading
from model import account
class Action:

    def __init__(self, accPtr, module):
        self.AccPtr = accPtr
        self.LoadedModule = module
        self.actionThread=threading.Thread(target=self.LoadedModule.test,kwargs={"email": self.AccPtr.Email,
                                                                        "password": self.AccPtr.Password})

    def Run(self):
        self.actionThread.start()




