import write_read_contact
import utils
import menu
import demo


msg="carnet de contact version 5"
menu.beau_menu(msg)
loop = True
while loop == True :

    contacts=write_read_contact.load_contacts()

    lst_menu=("1 pour ajouter un contacte", "2 pour lire la liste de contacts", "3 en suprimer un", "4 pour une backup", "5 chercher un contact", "6 pour stop")
    print("=================")
    for men in lst_menu :
        print(men)
    msg="Entrer l'option ici : "
    status = menu.belle_int_input(msg)

    if status == 0 :
        print("un nombre a été demander pas des lettres !!!!")


    elif status == 1 :
        newcontact=menu.menu_new_contact()
        contacts.append(newcontact)
        write_read_contact.write_contacts(contacts)
    
    elif status == 2 :
        msg=contacts
        menu.beau_menu(msg)

    elif status == 3 :
        ret=write_read_contact.delete_contact(contacts)
        contacts.pop(ret-1)
        write_read_contact.write_contacts(contacts)
    
    elif status == 4 :
        write_read_contact.backup(contacts)
    
    elif status == 5 :
        msg="Entrer le nom du contact que vous cherchez : "
        search=menu.belle_input(msg)
        contact=utils.search_contact(search, contacts)
        msg=contact
        menu.beau_menu(msg)
    
    elif status == 567 :
        demo.demo()
    else :
        loop = False