import pickle
class helperSerializer:
    def __init__(self, path):
        self.path=path

    def save(self, data):
        file= open(self.path,"wb")
        pickle.dump(data,file)
        file.close()

    def load(self):
        file= open(self.path,"rb")
        data=pickle.load(file)
        file.close()
        
        return data
