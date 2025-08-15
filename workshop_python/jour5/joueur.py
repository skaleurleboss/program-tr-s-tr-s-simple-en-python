print("algorithme de joueur")


def readFile(filename):
    f = open(filename, "r")
    line = f.read()
    print(line)

nombre_joueur = 2 
liste_joueurs = list() 

for loop in range(nombre_joueur):
    nom = input(f"Nom de jouer {loop+1} : ")
    MOM = float(input(f"MOM de joueur {loop+1} : "))
    joueur = {"nom" : nom, "MOM" : MOM }
    liste_joueurs.append(joueur)

print(liste_joueurs)


f = open("pdf.txt", "a", encoding="utf-8")

for j in liste_joueurs:
    txt = j["nom"] + ":" + str(j["MOM"]) 
    f.write(txt)

f.close()

readFile("pdf.txt")


exit()

'''


nomj2 = input("Nom de jouuer 2 : ")
MOMj2 = float(input("MOM de joueur 2 : "))
j2 = {"nom" : nomj2, "MOM" : MOMj2 }

nomj3 = input("Nom de jouuer 3 : ")
MOMj3 = float(input("MOM de joueur 3 : "))
j3 = {"nom" : nomj3, "MOM" : MOMj3 }

nomj4 = input("Nom de jouuer 4 : ")
MOMj4 = float(input("MOM de joueur 4 : "))
j4 = {"nom" : nomj4, "MOM" : MOMj4 }

nomj5 = input("Nom de jouuer 5 : ")
MOMj5 = float(input("MOM de joueur 5 : "))
j5 = {"nom" : nomj5, "MOM" : MOMj5 }

lj = [j1["nom"], j2["nom"], j3["nom"], j4["nom"], j5["nom"]]

print("Aujourdhui les joueur : ")
for lja in lj :
    print(lja)
print("vont s'affronter dans un matche épique")
lm = [j1["MOM"], j2["MOM"], j3["MOM"], j4["MOM"], j5["MOM"]]

la = list(j1.items()),list(j2.items()),list(j3.items()),list(j4.items()),list(j5.items())
print("ce match va êtres d'une intensitée incroyable grace au favorie de ce match avec un MOM de : ", max(lm))

with open("pdf.txt", "w", encoding="utf-8") as pdf:
    pdf.write(la)

'''
