from model.baseBehaviour import IBehaviourBase
import fbchat
from fbchat.models import *
from datetime import datetime
import pickle
import time


class AutoBirths(IBehaviourBase):
    def __init__(self):
        self.userBirthdays = dict()
        self.client = fbchat.Client("dddf@koszmail.pl", "przemekssie")



    def Run(self):
        self.userBirthdays = self.readPickle()
       # self.userBirthdays = dict()
       # self.userBirthdays.update({str(100004346340674): datetime.strptime('25 Nov 2017', '%d %b %Y')})
        now = datetime.now()
        now = now.replace(now.year, now.month, now.day, 0, 0, 0, 0)
        self.checkAllBirths(now)
        self.writePickle(self.userBirthdays)
        time.sleep(1000)
        while True:
            print('fuck')

    def writePickle(self, userBirthds):
        with open('birthdays.pickle', 'wb') as handle:
            pickle.dump(self.userBirthdays, handle, protocol=pickle.HIGHEST_PROTOCOL)

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
            return dat + (datetime.date(dat.year + 1, 1, 1) - datetime.date(dat.year, 1, 1))

bir = AutoBirths()
bir.Run()