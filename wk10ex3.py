import random


def create_dictionary(filename):
    f = open(filename)
    data = f.read()
    f.close()

    wordList = {}
    prev = '$'

    for curr in data.split():
        if prev not in wordList:
            wordList[prev] = []
        wordList[prev] += [curr]
        if curr[-1] not in '.?!':
            prev = curr
        else:
            prev = '$'

    return wordList


def generate_text(wordList, amount):
    prev = '$'
    assay = ''

    for _ in range(amount):
        word = random.choice(wordList[prev])
        assay += f'{word} '
        prev = word
        if word[-1] in '.?!':
            prev = '$'
    return assay


#
# Je gegenereerde essay van ongeveer 500 woorden (plak in de onderstaande triple-quoted strings):
#
"""
Bron: https://blackboard.hanze.nl/bbcswebdav/pid-5586298-dt-content-rid-64951674_2/courses/scmi.itvt.2109.1-2-inl-ictII-2122/Programmeren%20II/week10/wk10ex2.html
Ik dacht dit was 90% te veel uitleg, genoeg om een mooie text van te maken 😉

Een variabele met de lus break in de lus gebruiken als de gebruiker gekozen kolom niet te spelen! Merk op dat je moet dus afgelopen is een tweedimensionale lijst van hoe je mag ervan uitgaan dat je ze kan je break in het spel stoppen, het bord wordt opgeslagen. Je hoeft echter bestaan dat je een rij te houden: Deze methode moet ze kan testen door ' ', een voorbeeld zien van 7 bij 3... Je kan als dat zo is, moet de beurt en zijn in de tips over hoe deze vol is, herkennen, en moet de lus break kan kopiëren en daarna 'O'. Daarna moet de gebruiker een bord wordt opgeslagen. Vergeet niet te doen, en moet dus afgelopen is een if-else-statement staat. Toegegeven, dit maakt het aantal kolommen op een bericht worden met karakters die break in de stenen gespeeld wordt gespeeld wordt opgeslagen. Als het bord wordt op een paar keer het aantal methodes gebruiken. Merk op een geldig is. Ook moet er een leeg veld laten spelen, en plakken. Ook moet de tips over is, moet de tweedimensionale lijst een voorbeeld zien van ongeldige zetten, zowel 'X' en de tweedimensionale array met het voorkomen van de beurt en eieren dat je moet een rij nodig hebt om in de gebruiker om het spel Vier op dat zo is. Je hoeft echter bestaan dat zo verder... Je moet het aantal kolommen op een grote while-lus te spelen! Een stee mag ervan uitgaan dat zo is. Op die het spelen is een voorbeeld zien van karakters is; dit maakt het spelbord wordt opgeslagen. n deze vol is, moet elke steen in de beurt zijn. Als het spel wordt opgeslagen. 'X' is een tweedimensionale lijst van speler gewonnen heeft; als die het voorkomen van deze opgave ga je een laatste keer het bord verticaal opgesteld staat, de tips over is, moet ze controleren of als 'O' afwisselend aan de beurt zijn. Daarna moet de body van hoe je vier stenen niet de kolom vragen. De methode te testen te houden: Deze methode te winnen. Je kan als die break kan ook een rij te structureren. Je hoeft echter bestaan dat de klasse genaamd Board maken die break in de lus afgebroken worden afgedrukt en de body van speler O laten voorstellen door een paar belangrijke punten om uit een paar belangrijke punten om de gekozen kolom zetten. Op die speler X laten voorstellen door de tweedimensionale lijst van het spelbord voorstelt, en hiervoor add_move! Merk op het spel te doen, en zo is, moet ze kan testen door twee zetten onderstaande kleine lus gebruiken en plakken. Daarna moet elke steen in de andere speler X laten voorstellen door een bericht worden afgedrukt en kolommen op een leeg veld laten voorstellen door het spel een klasse Board. Als het wel lastig om een lus te testen door een 'X' en hiervoor add_move! Je moet er een geldig kolomnummer tot het spelbord voorstelt, en daarna 'O'. Vergeet niet over is,
"""
#
#
