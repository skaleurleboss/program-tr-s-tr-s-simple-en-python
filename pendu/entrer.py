def entrée() :
    loop_entrer = True
    while loop_entrer == True :
        lettre_proposee = input("proposer une lettre : ")
        if len(lettre_proposee) > 1 :
            print("1 seule lettre")
        else :
            loop_entrer = False
    return lettre_proposee