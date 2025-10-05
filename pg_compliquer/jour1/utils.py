import BeauMenu
import pathlib
from datetime import datetime
from urllib.request import urlopen
from html.parser import HTMLParser
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

def counterword(ph) :
    phl=ph.split(" ")
    dictio={}
    list_mot_deja_vu=[]
    for w in phl :
        if w in list_mot_deja_vu :
            valeur=dictio[w]
            valeur+=1
            dictio[w]=valeur

        else :
            list_mot_deja_vu.append(w)
            dictio[w] = 1
    dic_tuple=dictio.items()
    tuple_sorted=sorted(dic_tuple,key=lambda x:x[1], reverse=True)
    return tuple_sorted

def no_doublon(ph) :
    ph1=ph.split(" ")
    ph2=set(ph1)
    return ph2

def tree_first_word(ph) :
    ph1=ph.split(" ")
    list_mot=ph1[:3]
    ph1.reverse()
    list_mot2=ph1[:3]
    list_mot.extend(list_mot2)
    return list_mot

def write_word(ph) :
    with open("txt.txt", "w", encoding="utf-8") as f:
        f.write(ph)

def read_word() :
    with open("txt.txt", "r", encoding="utf-8") as f:
        contenu = f.read()
    return contenu

def lister_fichier():
    ph=BeauMenu.belle_input("entrer un chemin")
    for f in pathlib.Path(ph).rglob("*.txt"):
        return f

def meta_donnee(pa):
    p = pathlib.Path(pa)
    st = p.stat()

    file={"taille":st.st_size,"extension":p.suffix,"nom":p.stem,"modification":datetime.fromtimestamp(st.st_mtime)}
    return file

def scan_dir(pa, glob):
    pa = pathlib.Path()
    dir=[]
    for f in pa(".").rglob(glob):
        dir.append(f)
    return f

def file_weight(operator,sort_taille,dir) :
    file=meta_donnee(dir)
    taille=file[taille]
    final_file=[]
    for file in dir :
        file=meta_donnee(dir)
        taille=file[taille]
        if operator == "<=" :
            if taille <= sort_taille :
                final_file.append(file)
        if operator == ">=" :
            if taille >= sort_taille :
                final_file.append(file)
        if operator == "==" :
            if taille == sort_taille :
                final_file.append(file)
    return final_file

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_title = False
        self.in_h1 = False
        self.title = None
        self.links = []
        self.h1 = []

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self.in_title = True
        if tag == "h1":
            self.in_h1 = True
        if tag == "a":
            hrefs = [v for (k, v) in attrs if k == "href"]
            self.links.extend(hrefs)
            self.links = list(set(self.links))

    def handle_endtag(self, tag):
        if tag == "h1":
            self.in_h1 = False
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_h1:
            self.h1.append(data)
        if self.in_title:
            self.title = (self.title or "") + data.strip()

    def countInternalLink(self):
        counter = 0 
        for l in self.links:
            if l[0]=="/":
                counter = counter + 1
        return counter

    
def fetch_page(url: str) -> dict:
    with urlopen(url, timeout=5) as response:
        encoding = response.headers.get_content_charset() or "utf-8"
        html = response.read().decode(encoding)

    parser = PageParser()
    parser.feed(html)

    #sdir = slugify(url)
    # Create Directory
    #os.makedirs(sdir)

    return {
        "h1": parser.h1,
        "url": url,
        "title": parser.title,
        "links": parser.links,
        "count_internal": parser.countInternalLink()
    }



def check_url(url: str) -> bool:
    try:
        # on envoie une requête HEAD pour limiter la charge
        req = Request(url, method="HEAD")
        with urlopen(req, timeout=5) as resp:
            code = resp.getcode()
            # considère "ok" si code 200–299
            return 200 <= code < 300
    except HTTPError as e:
        print(f"HTTP error: {e.code} for {url}")
    except URLError as e:
        print(f"Connection error: {e.reason} for {url}")
    except Exception as e:
        print(f"Other error: {e}")
    return False


