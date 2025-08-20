import json
import os

def menu_new_contact() :
    nom=input("Entrer le nom de ce contact : ")
    age=input("Entrer l'age de ce contact : ")
    npa=input("Entrer la npa : ")
    rue=input("Entrer la rue : ")
    numm=input("Entrer le numéro de maison : ")
    num=input("Entrer le numéro de telephone : ")
    newcontact={"nom" : nom, "age" : age, "npa" : npa,"rue":rue,"numm":numm,"num":num}
    return newcontact

def search_contact(search, contacts) :
    for contact in contacts :
        if contact["nom"] == search :
            return contact
    return 