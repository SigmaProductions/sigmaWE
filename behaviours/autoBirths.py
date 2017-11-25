from model.baseBehaviour import IBehaviourBase
import fbchat
from fbchat.models import *
from datetime import datetime
import pickle
import time
import threading


class behaviourClass(IBehaviourBase):
    def __init__(self, email, password, kwargs):
        IBehaviourBase.__init__(email, password, kwargs)
        self.userBirthdays = dict()
        self.listening = ListeningBirthThreads(self)
        self.listening.Run()

    def Run(self):
        while True:
            self.userBirthdays = self.readPickle()
            now = datetime.now()
            now = now.replace(now.year, now.month, now.day, 0, 0, 0, 0)
            self.checkAllBirths(now)
            self.writePickle(self.userBirthdays)

    def writePickle(self, userBirthds):
        with open('birthdays.pickle', 'wb') as handle:
            pickle.dump(userBirthds, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def readPickle(self):
        with open('birthdays.pickle', 'rb') as handle:
            return pickle.load(handle)

    def checkAllBirths(self, now):
        for userID, dat in self.userBirthdays.items():
            if dat == now:
                self.client.send(message=Message("Wszystkiego najlepszego!"), thread_id=userID, thread_type=ThreadType.USER)
                self.userBirthdays.update({userID: self.addOneYear(dat)})

    def addOneYear(self, dat):
        try:
            return dat.replace(year = dat.year + 1)
        except ValueError:
            return dat + (datetime(dat.year + 1, 1, 1) - datetime(dat.year, 1, 1))

    def onMessage(self, author_id, message, thread_id, thread_type, **kwargs):
        births = self.readPickle()
        lines = message.split()
        if lines.__len__() == 4:
            userID = lines[0]
            day = lines[1]
            month = lines[2]
            year = lines[3]
            newDate = datetime(year)
            newDate = newDate.replace(year, month, day, 0, 0, 0, 0)
            births.update({userID: datetime.date(newDate)})
        self.writePickle(births)


class ListeningBirthThreads:
    def __init__(self, birthClient):
       # self.client = client
        self.listenThread = threading.Thread(target=birthClient.listen)

    def Run(self):
        self.listenThread.start()


