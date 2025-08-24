import end
import affichage__
import entrer
import mot_select
import BeauMenu
import os
import json
msg="Jeux du pendu betaV2"
BeauMenu.beau_menu(msg)

debug=False
loged=False
loopmenu=True
while loopmenu == True :
    

    lmsg=("1 pour lancer le jeux,","2 pour login,","3 pour créer un profil,","4 pour les state utilisateur,","5 pour stop.")
    status=BeauMenu.belle_list_int_inp(lmsg)

    if status == 1 :
        mot=mot_select.word_select()
        if debug == True :
            print(mot)

        essai_rate = 0
        lettre_proposees=[]
        loop=True
        while loop == True :
            lettre_proposee=entrer.entrée()
            lettre_proposees.append(lettre_proposee)
            affichage = ""
            trouver = True
            liste_lettres = list(mot)
            affichage, trouver, essai_rate = affichage__.affichage(essai_rate, affichage, liste_lettres, lettre_proposees, lettre_proposee, trouver)
            print(affichage)
            loop=end.end(trouver, essai_rate, mot, loop)

    elif status == 2 :
        if os.path.exists("utilisateurs.json") :
            with open("utilisateurs.json", "r", encoding="utf-8") as f:
                utilisateurs = json.load(f)
            print("=================")
            print("Entrer le nom du profil parmis ceux là : ")
            print("=================")
            i=1
            for l in utilisateurs :
                print(i," ",l["nom"])
                i+=1
            msg="Entrer la réponse ici : "
            utilisateur_number=BeauMenu.belle_int_input(msg)
            utilisateur=utilisateurs[utilisateur_number-1]
            loged=True



    elif status == 3 :
        msg="Entrer le nom d'utilisateur : "
        nom_dutilisateur_new=BeauMenu.belle_input(msg)
        utilisateur_new={"nom":nom_dutilisateur_new,"score":0}

        if not os.path.exists("utilisateurs.json"):
            open("utilisateurs.json", "x", encoding="utf-8")
            utilisateurs=[]  
        else :
            with open("utilisateurs.json", "r", encoding="utf-8") as f:
                utilisateurs = json.load(f)

        utilisateurs.append(utilisateur_new)
    
        with open("utilisateurs.json", "w", encoding="utf-8") as f:
            json.dump(utilisateurs, f, ensure_ascii=False, indent=4)


    elif status == 5 :
        loopmenu = False
        if loged == True :
            with open("utilisateurs.json", "w", encoding="utf-8") as f:
                json.dump(utilisateurs, f, ensure_ascii=False, indent=4)
    
    elif status == 567 :
        debug = True