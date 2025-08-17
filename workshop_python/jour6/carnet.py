import os
import json

def ecrire():
    nom=input("entrer le nom : ")
    adresse=input("entrer l'adresse")
    data = {"nom" : nom, "adresse" : adresse}
    with open("carnet.json", "a", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

loop = True
while loop == True :
    print("carnet d'adresse")
    status = float(input("1 pour lire le carnet 2 pour écrire 3 pour stop : "))
    if status == 1 :
        if os.path.exists("carnet.json") :
            with open("carnet.json", "r", encoding="utf8") as f:
                data=json.load(f)
                print("carnet : ", data)
        
        else :
            print("aucun numéro trouvé")

    elif status == 2 :
        nom=input("entrer le nom : ")
        adresse=input("entrer l'adresse")
        data = {"nom" : nom, "adresse" : adresse}
        with open("carnet.json", "a", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    elif status == 3:
        loop = False

    else :
        print("ce nombre n'existe pas")