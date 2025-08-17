import json
import os

def loadc() :
    with open("contact.json", "r", encoding="utf-8") as f:
            contact = json.load(f)
    return contact

def write(contact) :
     with open("contact.json", "w", encoding="utf-8") as f:
        json.dump(contact, f, indent=2, ensure_ascii=False)

print("carnet de contact version 3")
loop = True
while loop == True :

    if os.path.exists("contact.json") :
        contact = loadc()

    else :
        open("contact.json", "x", encoding="utf8")
        contact = []
            
    status=float(input("1 pour ajouter un contacte, 2 pour lire la liste de contact, 3 en suprimer un, 4 stop : "))


    if status == 1 :
            nom=input("Entrer le nom de ce contact : ")
            age=input("Entrer l'age de ce contact : ")
            npa=input("Entrer la npa : ")
            rue=input("Entrer la rue : ")
            numm=input("Entrer le numéro de maison : ")
            num=input("Entrer le numéro de telephone : ")
            newcontact={"nom" : nom, "age" : age, "npa" : npa,"rue":rue,"numm":numm,"num":num}
            contact.append(newcontact)
            write(contact)
    
    elif status == 2 :
         print(contact)

    elif status == 3 :
        i = 0
        for c in contact :
            print(f"{i+1} : {contact[i]}")
            i = i + 1
        ret = int(input("le quel voulez vous suprimez ? Entrer le numéro de liste : "))
        # on devrait tester que ret est pas trop grand ou trop petit
        contact.pop(ret-1)
        write(contact)
    
    elif status == 4 :
         loop = False