ortho = False

def fin (f,ortho) :
    f.close()
    ortho = True
    return f,ortho



while ortho == False :
    choix = input("read or write (and stop) : ")
    if choix == "read" :
        with open("txt.txt", "r", encoding="utf-8") as f:
            contenu = f.read()
            print(contenu)
            fin(f,ortho)

    elif choix == "write" :
        write = input("écriver : ")
        with open("txt.txt", "w", encoding="utf-8") as f:
            f.write(write)
            fin(f,ortho)

    elif choix == "stop" :
        print("stop")
        ortho = True

    else :
        print("vous avez mal orthographier")
        
        