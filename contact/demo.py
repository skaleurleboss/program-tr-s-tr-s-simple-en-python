import time
import menu


bob1 = r"""
   O
  /|\
  / \
 
Je suis Bob
"""
bob2 = r"""
   O
  /|\ _/
  / \
 
Au que oui !!
"""

bob3 = r"""
   O
  /|\
  / \
 
bah non car je suis sur signal !!!!
"""
bob4 = r"""
  \O/
   |
  / \
 
ouiiiiii !!!!
"""
bob5 = r"""
   O
  /|\
  / \
 
oui s'il vous plait
"""

def demo():
    msg="voici bob."
    menu.beau_menu(msg)
    print(bob1)
    time.sleep(5)

    msg="bob n'y connait rien en informatique."
    menu.beau_menu(msg)
    print(bob2)
    time.sleep(5)

    msg="bob veut classer ses contacts mais il ne fait pas confiance a ces boites multi-national."
    menu.beau_menu(msg)
    print(bob3)
    time.sleep(5)

    msg="c'est pour ca que andrea koerber a codé le gestionaire de contact v5 en open sources !!!!!!"
    menu.beau_menu(msg)
    print(bob4)
    time.sleep(5)

    msg="vous pouvez facillement gérer vos contacts et meme faire des backup tout ce que vous avez besoin !!!!!!!!"
    menu.beau_menu(msg)
    time.sleep(5)

    msg="faites comme Andrea Koerber, rendez bob heureux."
    menu.beau_menu(msg)
    print(bob5)
    time.sleep(5)

    print("retour dans le menu dans 5")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    return