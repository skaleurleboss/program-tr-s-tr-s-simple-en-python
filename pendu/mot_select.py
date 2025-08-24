import random
def word_select():
    liste_de_mot = (
        "contreattaque",
        "interception",
        "transmission",
        "feinte",
        "collectif",
        "pressing",
        "rotation",
        "suspension",
        "zonepress",
        "marquage"
    )



    min_val = 0
    max_val = len(liste_de_mot)
    nombre_aleatoire = random.randint (min_val, max_val)
    mot=liste_de_mot[nombre_aleatoire]
    return mot