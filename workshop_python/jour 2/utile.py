def addition(nombrea, nombreb) :
    nombrec = nombrea + nombreb
    return nombrec

def soustraction(nombrea, nombreb) :
    nombrec = nombrea - nombreb
    return nombrec

def demande_nombre():
    print("------------------")
    nombrea=int(input("nombre entier uniquement, entrer le nombre a"))
    print("------------------")
    nombreb=int(input("nombre entier uniquement, entrer le nombre b"))
    print("------------------")
    return nombrea, nombreb