from fbchat import Client
class IBehaviourBase(Client):
    def __init__(self,email,password, kwargs):
        """"abstract class being parent of every user implemented behaviour;
         it handles logging in and tasks on behaviour loader side"""
        self.kwargs=kwargs
        Client.__init__(self, email=email, password=password)
        self.Run()

    def Run(self):
        print("behaviour base abstract method invoked error")
        ## todo add exception here