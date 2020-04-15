# version 2, 15 avril 2020, B41VM
# A FAIRE
# retirerliste() - fait
# sauverfichier() - fait
# lirefichier() - fait
#     ajouter des le depart du logiciel   - fait
# afficher la liste courante  - fait

malistedenoms=[]

def ajouterdansliste():
    print("Veuillez fournir le nom a ajouter: ")
    lenom=input("Nom a ajouter: ")
    if lenom: # une chaine vide "", 0, ou liste vide [] == FAUX
        malistedenoms.append(lenom)
        
    return "Batman","robin",ajouterdansliste

def retirerdeliste():
    print("Veuillez fournir le nom a retirer: ")
    lenom=input("Nom a retirer: ")
    malistedenoms.remove(lenom)
    return 1

def sauverfichier():
    monfichier=open("malistedenoms.txt","w")
    for i in malistedenoms:
        monfichier.write(i)
        monfichier.write("\n")
    monfichier.close()
    
def lirefichier():
    global malistedenoms
    
    monfichier=open("malistedenoms.txt","r")
    #contenu=monfichier.read() # lis le fichier en entier, en un bloc de texte
    contenu=monfichier.readlines() # lis le fichier liste de ligne de texte
    monfichier.close()
    
    malistedenoms=[]
    
    for i in contenu:
        malistedenoms.append(i[:-1])  #  '[debut:fin] slicing prend une tranche de texte depart a arrive
    
def afficherlistedenoms():
    print()
    print("**** Liste courante ***")
    for i in malistedenoms:
        print(i)   
    print("*** Fin de la liste courante ***")
    print()

def menuprincipal():
    print("Faites votre choix: 1 pour ajouter, 2 pour retirer de la liste")
    print("                   3 pour sauver la liste, 4 pour afficher la liste")
    reponse=input("Votre choix svp: ")
    
    # Variante avec if et elif
    """
    if reponse=="1":    # pas de switch en python, facilement remplace par les dictionnaires
        rep=ajouterdansliste()
        print("RETOUR MULTIPLE",rep)
    elif reponse=="2":
        retirerdeliste()
    elif reponse=="3":
        sauverfichier()
    elif reponse=="4":
        afficherlistedenoms()
    else:
        return 0
    """
    
    # Variante avec distionnaire pour simuler switch
    reponsespossibles={"1":ajouterdansliste,
                       "2":retirerdeliste,
                       "3":sauverfichier,
                       "4":afficherlistedenoms,
                       }
    if reponse in reponsespossibles.keys():
        reponsespossibles[reponse]()
    else:
        return 0
    return 1

def main():
    lirefichier()
    n=1
    while n: # 0==faux, ""==faux, []== faux, None== faux, le reste test a vrai
        n=menuprincipal()


if __name__ == '__main__':
    print("Avant main ",malistedenoms)
    main()
    print("Apres main ", malistedenoms)
    print("Fin")