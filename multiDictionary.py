import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        self.dizio_ita = d.Dictionary().loadDictionary("resources/Italian.txt")
        self.dizio_eng = d.Dictionary().loadDictionary("resources/English.txt")
        self.dizio_spa = d.Dictionary().loadDictionary("resources/Spanish.txt")


    def printDic(self, language):
        if language == "italian":
            self.dizio_ita.printAll()
        elif language == "english":
            self.dizio_eng.printAll()
        elif language == "spanish":
            self.dizio_spa.printAll()

    def searchWord(self, words, language):
        if language == "italian":
            parole = words.split(" ")
            paroleSbagliate = []
            for i in parole:
                parolar = rw.RichWord(i)
                if self.dizio_ita.__contains__(i):
                    parolar.corretta = True
                else:
                    paroleSbagliate.append(i)
            return paroleSbagliate
        if language == "english":
            parole = words.split(" ")
            paroleSbagliate = []
            for i in parole:
                parolar = rw.RichWord(i)
                if self.dizio_eng.__contains__(i):
                    parolar.corretta = True
                else:
                    paroleSbagliate.append(i)
            return paroleSbagliate
        if language == "spanish":
            parole = words.split(" ")
            paroleSbagliate = []
            for i in parole:
                parolar = rw.RichWord(i)
                if self.dizio_spa.__contains__(i):
                    parolar.corretta = True
                else:
                    paroleSbagliate.append(i)
            return paroleSbagliate

    def searchWordLinear(self, words, language):
        paroleTrovate = []
        if language == "italian":
            parole = words.split(" ")
            for i in parole:
                if self.dizio_ita.__contains__(i):
                    paroleTrovate.append(i)
            return paroleTrovate
        elif language == "english":
            parole = words.split(" ")
            for i in parole:
                if self.dizio_eng.__contains__(i):
                    paroleTrovate.append(i)
            return paroleTrovate
        elif language == "spanish":
            parole = words.split(" ")
            for i in parole:
                if self.dizio_spa.__contains__(i):
                    paroleTrovate.append(i)
            return paroleTrovate


    def searchWordDichotomic(self, words, language):
        paroleTrovate = []
        min = 0
        max = 0
        if language == "italian":
            parole = words.split(" ")
            medio = int(len(self.dizio_ita)/2)
            for i in parole:
                if i == self.dizio_ita[medio]:
                    paroleTrovate.append(i)
                    print("Parola trovata")
                elif i > self.dizio_ita[medio]:
                    max = medio
                    for p in self.dizio_ita[min:max]:
                        if p == i:
                            paroleTrovate.append(i)
                            print("Parola trovata")
                elif i < self.dizio_ita[int(medio)]:
                    min = medio
                    max = len(self.dizio_ita)
                    for p in self.dizio_ita[min:max]:
                        if p == i:
                            paroleTrovate.append(p)
                            print("Parola trovata")
        if language == "english":
            parole = words.split(" ")
            medio = int(len(self.dizio_eng)/2)
            for i in parole:
                if i == self.dizio_eng[medio]:
                    paroleTrovate.append(i)
                    print("Parola trovata")
                elif i > self.dizio_eng[medio]:
                    max = medio
                    for p in self.dizio_eng[min:max]:
                        if p == i:
                            paroleTrovate.append(i)
                            print("Parola trovata")
                elif i < self.dizio_eng[medio]:
                    min = medio
                    max = len(self.dizio_eng)
                    for p in self.dizio_ita[min:max]:
                        if p == i:
                            paroleTrovate.append(p)
                            print("Parola trovata")
        if language == "spanish":
            parole = words.split(" ")
            medio = int(len(self.dizio_spa)/2)
            for i in parole:
                if i == self.dizio_spa[medio]:
                    paroleTrovate.append(i)
                    print("Parola trovata")
                elif i > self.dizio_spa[medio]:
                    max = medio
                    for p in self.dizio_spa[min:max]:
                        if p == i:
                            paroleTrovate.append(i)
                            print("Parola trovata")
                elif i < self.dizio_spa[medio]:
                    min = medio
                    max = len(self.dizio_spa)
                    for p in self.dizio_spa[min:max]:
                        if p == i:
                            paroleTrovate.append(p)
                            print("Parola trovata")
        return paroleTrovate
