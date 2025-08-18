
import utils


print("carnet de contact version 4")
loop = True
while loop == True :

    contacts=utils.load_contacts()
            
    status = int(input("1 pour ajouter un contacte, 2 pour lire la liste de contacts, 3 en suprimer un, 4 pour une backup, 5 chercher un contact, 6 pour stop : "))

    if status == 1 :
        newcontact=utils.menu_new_contact()
        contacts.append(newcontact)
        utils.write_contacts(contacts)
    
    elif status == 2 :
        print(contacts)

    elif status == 3 :
        ret=utils.delete_contact(contacts)
        contacts.pop(ret-1)
        utils.write_contacts(contacts)
    
    elif status == 4 :
        utils.backup(contacts)
    
    elif status == 5 :
        search=input("Entrer le nom du contact que vous cherchez : ")
        contact=utils.search_contact(search, contacts)
        print(contact)
    
    else :
        loop = False