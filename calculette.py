(stop) = ("non")

while stop != ("oui") :
 
    print ("bienvenue dans calcullette taper : +, -, * ou /")

    (symbole) = input()

    (chifre1) = float(input("1er nombre : "))

    (chifre2) = float(input("2ème nombre : "))

    if (symbole) ==("+") :
        print((chifre1) + (chifre2))

    elif (symbole) == ("-") :
        print((chifre1) - (chifre2))

    elif (symbole) == ("*") :
        print((chifre1) * (chifre2))

    elif (symbole) == ("/") :
        print (chifre1) / (chifre2)

    (stop) = input("arrêter ? : ")





