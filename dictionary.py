class Dictionary:
    def __init__(self, dizionario=None):
        if dizionario is None:
            dizionario = []
        self.dizionario = dizionario


    def loadDictionary(self,path):
        diziolingua = []
        with open(path, 'r', encoding="UTF-8") as infile:
            for line in infile:
                parola = ""
                for i in line:
                    if i != "\n":
                        parola += i
                diziolingua.append(parola)
            return diziolingua

    def printAll(self):
        for riga in self.dizionario:
            print(riga)


    @property
    def dict(self):
        return self._dict