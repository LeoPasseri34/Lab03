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
        dizionario = []
        paroleTrovate = []
        if language == "italian":
            dizionario = self.dizio_ita
        elif language == "english":
            dizionario = self.dizio_eng
        elif language == "spanish":
            dizionario = self.dizio_spa

        parole = words.split(" ")
        for parola in parole:
            minimo = 0
            massimo = len(dizionario)-1
            trovata = False

            while minimo <= massimo:
                medio = (massimo+massimo)//2
                parolaMedia = dizionario[medio]

                if parola == parolaMedia:
                    trovata = True
                    paroleTrovate.append(parola)
                    break
                elif parola > parolaMedia:
                    minimo = medio+1
                else:
                    massimo = medio-1

            if not trovata:
                print(f"La parola {parola} non è stata trovata nel dizionario")

        return paroleTrovate