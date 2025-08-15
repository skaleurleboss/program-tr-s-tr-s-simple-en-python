boucle = True

essai = 0

while boucle == True and essai != 6:

    password = input("password : ")

    if password == "1223admin" :
        print("bienvenu admin")
        boucle = False

    else :
        print("accès refusé")
        essai += 1
        print("il reste ", 6-essai, "essais")

    if essai == 6 :
        print("réésaye dans 5 min")