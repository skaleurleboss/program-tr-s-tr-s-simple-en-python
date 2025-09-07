import BeauMenu

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
