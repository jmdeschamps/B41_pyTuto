
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
        # VARIANTE
        #print("annee: ",repsepare[2][:-1])  # on slice du debut jusqu'au caracteres final moins 1
        #print("titre: ",repsepare[0],"\n")  # on imprime une autre ligne comme separateur

if __name__ == '__main__':
    contenu=liredocument()
    affichercontenu(contenu)