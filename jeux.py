import random

(min_val) = 0

(max_val) = 20

(etat) = ("non")

while etat != ("oui") :

    (etatdejeu) = input("voulez vous joué ? : ")

    if (etatdejeu) == ("oui") :
        
        (nombre_aleatoire) = random.randint(min_val, max_val)

        (terminerlejeu) = ("non")

        (essai) = 0

        while terminerlejeu != ("oui") :

            (nombre) = float((input("votre nombre : ")))
            if (nombre) > (nombre_aleatoire):

                print("trop grand")

                (essainew) = (essai) + 1

                (essai) = (essainew)

            elif (nombre) < (nombre_aleatoire):

                print("trop petit")

                (essainew) = (essai) + 1

                (essai) = (essainew)

            else :

                print("gagné")

                print("vous l'avez fait en : ") 
                
                (essainew) = (essai) + 1

                (essai) = (essainew)

                print(essai)

                (terminerlejeu) = ("oui")
            
    elif (etatdejeu) == ("non"):

        (etat) = ("oui")
