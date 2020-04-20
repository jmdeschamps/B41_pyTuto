## -*- Encoding: UTF-8 -*-  

####### Transformation OOP et organisation Modele-Vue-Controleur dit MVC #####
###   Principe MVC
#    Les ordinateurs utilisent généralement les mêmes entrées/sorties (E/S)
#    quel que soit le type de programme, à savoir:
#    le clavier et la souris pour l'entrée
#    l'écran pour la sortie
#    NOTE: Oui, il y a le son, il y a des manettes, caméras etc qui peuvent aussi servir
#    mais nous garderons cela simple pour l'instant
#    Par contre, les logiciels (qui utilisent ces E/S) peuvent être d'une extrême variabilité
#    Gestion de comptes bancaires, traitement de texte, gestion de machines industrielles, jeux, etc
#    
#    But du MVC -> garder l'intelligence d'affaire (MODÈLE) comme les traitements ou les calculs des domaines
#    d'application SÉPARÉE de la logique d'affichage et de saisie de l'information (VUE)
#
#    On peut ainsi penser qu'un logiciel comptable, qui suit des règles de comptabilité,
#    effectue ses tâches de la même façon, que la commande ait été donnée en cliquant sur un bouton,
#    par une commande verbale, ou par les caractères tapés au clavier.
#    De manière similaire, les résultats de traitements d'affaires, peuvent s'afficher en tableau,
#    en formulaire, en graphique, etc.
#
#    On tentera de grouper ensemble les fonctions pertinentes à l'intelligence d'affaire (modules,
#    classes et fonctions)
#    Par ailleurs, les fonctions d'écoute ("listener" de bouton et al), console.input(),
#    ainsi que les fonctions d'affichage (print, insertText, drawPie) seront elles aussi
#    groupées ensemble, prêtes à servir.
#    
#    Afin de bien découpler ces deux univers (domaine affaire vs E/S), on introduit un entremetteur,
#    le contrôleur, dont le travail est d'assurer la communication entre les deux autres sections. 



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
class GestionBDFilm():
    def __init__(self):
        self.malistedenoms=[] #
class Controleur():
    def __init__(self):
        self.modeleaffaire=GestionBDFilm()  # on cr�e un objet responsable du traitement des donn�es
        self.entreesortie=GestionES()   # on cr�e un objet responsable des entr�es/sorties

if __name__ == '__main__':
    moncontroleur=Controleur()