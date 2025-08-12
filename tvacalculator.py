(eta) = 0

while (eta) != (1) :
    (nombre) = float(input("prix (CHF) : "))
    (tva) = input("(faire stop pour arrêter) ttc ou hors taxes : ")

    if (tva) == ("ttc") :
        print((nombre) - 8,1)
        print(nombre)

    elif (tva) == ("hors taxes"):
        print(nombre)
        print((nombre) + 8,1)

    elif (tva) == ("stop"):
        break

    else :
        print("taper quelque chose de correcte")