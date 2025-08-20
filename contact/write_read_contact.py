import os
import json

def load_contacts() :
    if os.path.exists("contact.json") :
        try :
            with open("contact.json", "r", encoding="utf-8") as f:
                contacts = json.load(f)
        except Exception :
            contacts=[]

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

def delete_contact(contacts) :
    i = 0
    for c in contacts :
        print("=================")
        print(f"{i+1} : {contacts[i]}")
        i = i + 1
    print("=================")
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