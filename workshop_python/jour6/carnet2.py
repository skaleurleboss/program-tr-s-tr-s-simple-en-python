import json
import os

FICHIER_CONTACTS = "contacts.json"

def charger_contacts():
    """Charge les contacts depuis le fichier JSON, ou retourne une liste vide si le fichier n'existe pas."""
    if os.path.exists(FICHIER_CONTACTS):
        with open(FICHIER_CONTACTS, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    else:
        return []

def sauvegarder_contacts(contacts):
    """Sauvegarde la liste des contacts dans le fichier JSON."""
    with open(FICHIER_CONTACTS, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=4, ensure_ascii=False)

def ajouter_contact():
    """Demande à l'utilisateur d'entrer un contact et l'ajoute à la liste."""
    nom = input("Nom : ")
    prenom = input("Prénom : ")
    telephone = input("Téléphone : ")

    contact = {
        "nom": nom,
        "prenom": prenom,
        "telephone": telephone
    }

    contacts = charger_contacts()
    contacts.append(contact)
    sauvegarder_contacts(contacts)
    print("✅ Contact ajouté avec succès.")

def afficher_contacts():
    """Affiche tous les contacts stockés."""
    contacts = charger_contacts()
    if not contacts:
        print("📭 Aucun contact enregistré.")
    else:
        print("\n📒 Liste des contacts :")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['prenom']} {contact['nom']} - 📞 {contact['telephone']}")

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Ajouter un contact")
        print("2. Afficher les contacts")
        print("3. Quitter")

        choix = input("Choix : ")

        if choix == "1":
            ajouter_contact()
        elif choix == "2":
            afficher_contacts()
        elif choix == "3":
            print("👋 Au revoir !")
            break
        else:
            print("❌ Choix invalide, essaie encore.")

if __name__ == "__main__":
    menu()
