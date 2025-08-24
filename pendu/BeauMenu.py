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
def belle_list_int_inp(lmsg) :
    print("=================")
    for msg in lmsg :
        print(msg)
    print("=================")
    msgc=int(input("Entrer la réponse ici : "))
    return msgc

def belle_list_inp(lmsg) :
    print("=================")
    for msg in lmsg :
        print(msg)
    print("=================")
    msgc=input("Entrer la réponse ici : ")
    return msgc
