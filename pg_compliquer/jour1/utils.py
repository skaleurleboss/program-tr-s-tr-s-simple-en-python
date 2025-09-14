import BeauMenu
import pathlib
from datetime import datetime

def counterword() :
    ph=BeauMenu.belle_input("entrer une phrase : ")
    phl=ph.split(" ")
    dictio={}
    list_mot_deja_vu=[]
    for w in phl :
        if w in list_mot_deja_vu :
            valeur=dictio[w]
            valeur+=1
            dictio[w]=valeur

        else :
            list_mot_deja_vu.append(w)
            dictio[w] = 1
    dic_tuple=dictio.items()
    tuple_sorted=sorted(dic_tuple,key=lambda x:x[1], reverse=True)
    for msg in tuple_sorted :
        BeauMenu.beau_menu(msg)

def no_doublon() :
    ph=BeauMenu.belle_input("entrer une phrase : ")
    ph1=ph.split(" ")
    ph2=set(ph1)
    print(ph2)
    return ph2

def tree_first_word() :
    ph=BeauMenu.belle_input("entrer une phrase : ")
    ph1=ph.split(" ")
    list_mot=ph1[:3]
    ph1.reverse()
    list_mot2=ph1[:3]
    list_mot.extend(list_mot2)
    print(list_mot)

def write_word() :
    ph=BeauMenu.belle_input("entrer une phrase : ")
    with open("txt.txt", "w", encoding="utf-8") as f:
        f.write(ph)

def read_word() :
    with open("txt.txt", "r", encoding="utf-8") as f:
        contenu = f.read()
    print(contenu)

def lister_fichier():
    ph=BeauMenu.belle_input("entrer un chemin")
    for f in pathlib.Path(ph).rglob("*.txt"):
        print(f)

def meta_donnee():
    p = pathlib.Path("txt.txt")
    st = p.stat()

    print("Taille:", st.st_size, "octets")
    print("Extension:", p.suffix)
    print("Nom:", p.stem)
    print("Modifié:", datetime.fromtimestamp(st.st_mtime))

write_word()
read_word()
lister_fichier()
meta_donnee()