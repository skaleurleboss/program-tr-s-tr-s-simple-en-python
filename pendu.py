import random

print("Jeux du pendu.")

liste_de_mot=["pierre", "andrea", "pendu", "pilote", "pomme"]
min_val = 0
max_val = 4
nombre_aleatoire = random.randint (min_val, max_val)
mot=liste_de_mot[nombre_aleatoire]

essai_rate = 0
lettre_proposees=[]
loop=True
print(mot)
while loop == True :
    loop_entrer = True
    while loop_entrer == True :
        lettre_proposee = input("proposer une lettre : ")
        if len(lettre_proposee) > 1 :
            print("1 seul lettre")
        else :
            loop = False
    lettre_proposees.append(lettre_proposee)
    affichage = ""
    liste_lettres = list(mot)
    for l in liste_lettres:
        if l in lettre_proposees:
            affichage = affichage + l + " "
        else :
            affichage += "_ "
    if lettre_proposee not in liste_lettres :
        essai_rate += 1

    print(affichage)

    if essai_rate == 10 :
        print("perdu le mot était :",mot)
        loop == False
    
    if essai_rate == 1 :
        print(
        """                       
                               
                               
                               
                               
                               
                               
                               
                               
        _______________________""")
    elif essai_rate == 2 :
        print(
        """            !          
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
        """            +---------",
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
        """            +----------
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
        """            +----------
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
        """            +----------
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
        """            +----------
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
        """            +----------
                    ! /       !
                    !/        !
                    !         0
                    !        /!\
                    !          
                    !          
                    !          
                    !          
        ____________+__________""")
    elif essai_rate == 9 :
        print(
        """            +----------
                    ! /       !
                    !/        !
                    !         0
                    !        /!\
                    !        / 
                    !          
                    !          
                    !          
        ____________+__________""")
    elif essai_rate == 10 :
        print(
        """            +----------
                    ! /       !
                    !/        !
                    !         0
                    !        /!\
                    !        / \
                    !          
                    !          
                    !          
        ____________+__________""")
    
