import json
import os

def load_contacts() :
    if os.path.exists("contact.json") :
        with open("contact.json", "r", encoding="utf-8") as f:
            contacts = json.load(f)

    else :
        open("contact.json", "x", encoding="utf8")
        contacts = []
    
    return contacts

def write_contacts(contacts) :
    if os.path.exists("contact.json"):
        with open("contact.json", "w", encoding="utf-8") as f:
            json.dump(contacts, f, indent=2, ensure_ascii=False)
    else:
        open("contact.json", "x", encoding="utf8")
        with open("contact.json", "w", encoding="utf-8") as f:
            json.dump(contacts, f, indent=2, ensure_ascii=False)
    return
        


def menu_new_contact() :
    nom=input("Entrer le nom de ce contact : ")
    age=input("Entrer l'age de ce contact : ")
    npa=input("Entrer la npa : ")
    rue=input("Entrer la rue : ")
    numm=input("Entrer le numéro de maison : ")
    num=input("Entrer le numéro de telephone : ")
    newcontact={"nom" : nom, "age" : age, "npa" : npa,"rue":rue,"numm":numm,"num":num}
    return newcontact

def delete_contact(contacts) :
    i = 0
    for c in contacts :
        print(f"{i+1} : {contacts[i]}")
        i = i + 1
    ret = int(input("le quel voulez vous suprimez ? Entrer le numéro de liste : "))
    return ret

def backup(contacts) :
    if os.path.exists("backup.json"):
        with open("backup.json", "w", encoding="utf-8") as f:
            json.dump(contacts, f, indent=2, ensure_ascii=False)
    else:
        open("backup.json", "x", encoding="utf8")
        with open("backup.json", "w", encoding="utf-8") as f:
            json.dump(contacts, f, indent=2, ensure_ascii=False)
    return

def search_contact(search, contacts) :
    for contact in contacts :
        if contact["nom"] == search :
            return contact
    return 