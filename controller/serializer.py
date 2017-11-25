import pickle
class helperSerializer:
    def __init__(self, path):
        self.path=path

    def save(self, fileName, data):
        file= open(self.path,"wb")
        pickle.dump(data+fileName,file)
        file.close()

    def load(self,fileName):

        file= open(self.path+fileName,"rb")
        data=pickle.load(file)
        file.close()

        return data
