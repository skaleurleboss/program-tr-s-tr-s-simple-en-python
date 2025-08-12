from utile import addition
from utile import soustraction
from utile import demande_nombre

print("===========Calculette===========")

choix=input("1 pour adition 2 pour soustraction")

if choix == "1" :
    n1,n2 = demande_nombre()
    nombrec=addition(n1 , n2)
    print(nombrec)


if choix == "2" :
    n1,n2 = demande_nombre()
    nombrec=soustraction(n1 , n2)
    print(nombrec)