import datetime
import string
import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.multi = md.MultiDictionary()

    def handleSentence(self, txtIn, language):
        tic = datetime.datetime.now()
        testo = replaceChars(txtIn)
        sbagliate = md.MultiDictionary().searchWord(testo, language)
        toc = datetime.datetime.now()
        print(f"Le parole sbagliate sono {len(sbagliate)} calcolate in {toc-tic}:")
        for i in sbagliate:
            print(i)

    def handleSentenceLinear(self, txtIn, language):
        tic = datetime.datetime.now()
        testo = replaceChars(txtIn)
        parolaTrovata = md.MultiDictionary().searchWordLinear(testo, language)
        toc = datetime.datetime.now()
        print(f"Le parole trovate con la ricerca lineare in {toc - tic} sono:")
        for p in parolaTrovata:
            print(p)

    def handleSentenceDichotomic(self, txtIn, language):
        tic = datetime.datetime.now()
        testo = replaceChars(txtIn)
        parolaTrovata = md.MultiDictionary().searchWordDichotomic(testo, language)
        toc = datetime.datetime.now()
        print(f"Le parole trovate con la ricerca dicotomica in {toc - tic} sono:")
        return parolaTrovata

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text
