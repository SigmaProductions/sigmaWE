from model.baseBehaviour import IBehaviourBase
import fbchat
from fbchat.models import *
import threading



class behaviourClass(IBehaviourBase):

    def LoadAccountsFromConversation(self):
        self.groupinfo = self.fetchGroupInfo(self.CONF_ID)
        self.ParticipantsID = self.groupinfo[self.CONF_ID].participants




    def Run(self):
        self.listOfIds = []
        self.CONF_ID = self.kwargs["CONFID"]
        self.LoadAccountsFromConversation()
        ##self.send(Message(text='This is a @mention', mentions=[Mention(self.CONF_ID, offset=10, length=8)]),
                    ##thread_id=self.CONF_ID, thread_type=fbchat.ThreadType.GROUP)
        while(True):
            self.listen()


    def onMessage(self, mid=None, author_id=None, message=None, message_object=None, thread_id=None, thread_type=ThreadType.GROUP, ts=None, metadata=None, msg=None, **kwargs):
        if(message_object.text.lower() == "@everyone"):
            for par in self.ParticipantsID:
                accountToLoad = self.fetchUserInfo(par)
                self.nameToLoad = accountToLoad[par].first_name
                self.send(Message(text='@%s' % (self.nameToLoad),
                                  mentions=[Mention(self.CONF_ID, offset=0, length=len(self.nameToLoad) + 1)]),
                          thread_id=self.CONF_ID, thread_type=fbchat.ThreadType.GROUP)
