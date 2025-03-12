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
        elif language == "english":
            parole = words.split(" ")
            paroleSbagliate = []
            for i in parole:
                parolar = rw.RichWord(i)
                if self.dizio_eng.__contains__(i):
                    parolar.corretta = True
                else:
                    paroleSbagliate.append(i)
        elif language == "spanish":
            parole = words.split(" ")
            paroleSbagliate = []
            for i in parole:
                parolar = rw.RichWord(i)
                if self.dizio_spa.__contains__(i):
                    parolar.corretta = True
                else:
                    paroleSbagliate.append(i)
            return paroleSbagliate


