  ## DE RETOUR 

malistedenoms=[]

def ajouterdansliste():
    print("Veuillez fournir le nom: ")
    lenom=input("Nom: ")
    if lenom: # une chaine vide "", 0, ou liste vide [] == FAUX
        malistedenoms.append(lenom)

def retirerdeliste():
    pass

def menuprincipal():
    print("Faites votre choix: 1 pour ajouter, 2 pour retirer de la liste")
    reponse=input("Votre choix svp: ")
    if reponse=="1":
        ajouterdansliste()
    elif reponse=="2":
        retirerdeliste()
    else:
        return 0
    return 1

def main():
    n=1
    while n:
        n=menuprincipal()


if __name__ == '__main__':
    print("Avant main ",malistedenoms)
    main()
    print("Apres main ", malistedenoms)
    print("Fin")