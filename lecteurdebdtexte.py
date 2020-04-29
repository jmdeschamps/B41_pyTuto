
def liredocument():
    fiche=open("libfilm.txt")
    print(fiche)
    contenu=fiche.readlines()[1:]  # utilise le slice '[depart:fin]' sur le resultat du split
    fiche.close()
    print(contenu)
    return contenu

def affichercontenu(texte):
    for i in texte:
        repsepare=i.split(";:;")
        print("annee: ",repsepare[2])
        print("titre: ",repsepare[0])

if __name__ == '__main__':
    contenu=liredocument()
    affichercontenu(contenu)