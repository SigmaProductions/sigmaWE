import pickle
class helperSerializer:
    def __init__(self, path):
        self.path=path

    def save(self, dataName, data):
        file= open(self.path,"wb")
        pickle.dump(data+dataName,file)
        file.close()

    def load(self,dataName):

        file= open(self.path+dataName,"rb")
        data=pickle.load(file)
        file.close()

        return data
