def affichage(essai_rate, affichage, liste_lettres, lettre_proposees, lettre_proposee, trouver) :
    for l in liste_lettres:
            
        if l in lettre_proposees:
            affichage = affichage + l + " "
        else :
            affichage += "_ "
            trouver = False
    if lettre_proposee not in liste_lettres :
        essai_rate += 1
    return affichage, trouver, essai_rate