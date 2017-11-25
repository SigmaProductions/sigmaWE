import threading

class Action:
    def __init__(self, accPtr, module,kwargs):

        self.AccPtr = accPtr
        self.LoadedModule = module
        self.Kwargs=kwargs
        self.actionThread=threading.Thread(target=self.LoadedModule.behaviourClass,kwargs={"email": self.AccPtr.Email,
                                                                                "password": self.AccPtr.Password,
                                                                                "kwargs":self.Kwargs})

    def Run(self):
        self.actionThread.start()


    def Stop(self):
        self.actionThread._stop()




