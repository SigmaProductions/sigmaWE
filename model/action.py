import threading
from model import account
class Action:

    def __init__(self, accPtr, moduleName):
        self.AccPtr = accPtr
        self.LoadedModule = moduleName

    def Run(self):
        threading.Thread(target=self.LoadedModule,kwargs={"email": self.AccPtr.email, "password": self.AccPtr.password}).start()




