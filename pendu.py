import random

print("Jeux du pendu.")

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
max_val = 4
nombre_aleatoire = random.randint (min_val, max_val)
mot=liste_de_mot[nombre_aleatoire]

essai_rate = 0
lettre_proposees=[]
loop=True
while loop == True :
    loop_entrer = True
    while loop_entrer == True :
        lettre_proposee = input("proposer une lettre : ")
        if len(lettre_proposee) > 1 :
            print("1 seule lettre")
        else :
            loop_entrer = False
    lettre_proposees.append(lettre_proposee)
    affichage = ""
    trouver = True
    liste_lettres = list(mot)
    for l in liste_lettres:
        
        if l in lettre_proposees:
            affichage = affichage + l + " "
        else :
            affichage += "_ "
            trouver = False
    if lettre_proposee not in liste_lettres :
        essai_rate += 1

    print(affichage)

    if trouver == True :
        print("Gagnéé !!!!!")
        loop=False
    
    if essai_rate == 1 :
        print(
        """                       
                               
                               
                               
                               
                               
                               
                               
                               
        _______________________""")
    elif essai_rate == 2 :
        print(
        """
                    !          
                    !          
                    !          
                    !          
                    !          
                    !          
                    !          
                    !          
                    !          
        ____________+__________""")
    elif essai_rate == 3 :
        print(
        """
                    +---------
                    !          
                    !          
                    !          
                    !          
                    !          
                    !          
                    !          
                    !          
        ____________+__________""")
    elif essai_rate == 4 :
        print(
        """
                    +----------
                    ! /        
                    !/         
                    !          
                    !          
                    !          
                    !          
                    !          
                    !          
        ____________+__________""")
    
    elif essai_rate == 5 :
        print(
        """
                    +----------
                    ! /       !
                    !/        !
                    !          
                    !          
                    !          
                    !          
                    !          
                    !          
        ____________+__________""")
    elif essai_rate == 6 :
        print(
        """
                    +----------
                    ! /       !
                    !/        !
                    !         0
                    !          
                    !          
                    !          
                    !          
                    !          
        ____________+__________""")
    elif essai_rate == 7 :
        print(
        """
                    +----------
                    ! /       !
                    !/        !
                    !         0
                    !         !
                    !          
                    !          
                    !          
                    !          
        ____________+__________""")
    elif essai_rate == 8 :
        print(
        """
                    +----------
                    ! /       !
                    !/        !
                    !         0
                    !        /!
                    !          
                    !          
                    !          
                    !          
        ____________+__________""")
    elif essai_rate == 9 :
        print(
        """
                    +----------
                    ! /       !
                    !/        !
                    !         0/
                    !        /!
                    !          
                    !          
                    !          
                    !          
        ____________+__________""")
    elif essai_rate == 10 :
        print(
        """
                    +----------
                    ! /       !
                    !/        !
                    !         0/
                    !        /!
                    !        / 
                    !          
                    !          
                    !          
        ____________+__________""")
    elif essai_rate == 11 :
        print(
        """
                    +----------
                    ! /       !
                    !/        !
                    !         0/
                    !        /!/
                    !        / 
                    !          
                    !          
                    !          
        ____________+__________""")

        print("perdu le mot était : ", mot)
