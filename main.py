import spellchecker

sc = spellchecker.SpellChecker()

while(True):
    sc.printMenu()

    txtIn = input()
    # Add input control here!

    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input().lower()
        sc.handleSentence(txtIn,"italian")
        print("-------------------------------------")
        sc.handleSentenceLinear(txtIn,"italian")
        print("-------------------------------------")
        sc.handleSentenceDichotomic(txtIn,"italian")
        continue

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input().lower()
        sc.handleSentence(txtIn,"english")
        print("-------------------------------------")
        sc.handleSentenceLinear(txtIn,"english")
        print("-------------------------------------")
        sc.handleSentenceDichotomic(txtIn,"english")
        continue

    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input().lower()
        sc.handleSentence(txtIn,"spanish")
        print("-------------------------------------")
        sc.handleSentenceLinear(txtIn,"spanish")
        print("-------------------------------------")
        sc.handleSentenceDichotomic(txtIn,"spanish")
        continue

    if int(txtIn) == 4:
        break


