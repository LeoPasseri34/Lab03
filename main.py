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
        sc.handleSentenceLinear(txtIn,"italian")
        sc.handleSentenceDichotomic(txtIn,"italian")
        continue

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input().lower()
        sc.handleSentence(txtIn,"english")
        sc.handleSentenceLinear(txtIn,"english")
        sc.handleSentenceDichotomic(txtIn,"english")
        continue

    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input().lower()
        sc.handleSentence(txtIn,"spanish")
        sc.handleSentenceLinear(txtIn,"spanish")
        sc.handleSentenceDichotomic(txtIn,"spanish")
        continue

    if int(txtIn) == 4:
        break


