def menu_new_contact() :
    nom=belle_input("Entrer le nom de ce contact : ")
    age=belle_input("Entrer l'age de ce contact : ")
    npa=belle_input("Entrer la npa : ")
    rue=belle_input("Entrer la rue : ")
    numm=belle_input("Entrer le numéro de maison : ")
    num=belle_input("Entrer le numéro de telephone : ")
    newcontact={"nom" : nom, "age" : age, "npa" : npa,"rue":rue,"num_de_maison":numm,"num":num}
    return newcontact

def beau_menu(msg) :
    print("=================")
    try :
        print(msg.capitalize())
    except Exception :
        print(msg)
    return

def belle_input(msg) :
    print("=================")
    msgc=input(msg.capitalize())
    return msgc

def belle_int_input(msg) :
    print("=================")
    try :
        msgc=int(input(msg))
        return msgc
    except ValueError :
        return 0