##  ATTENTION
#    voici tout le code qu'on a produit lors de l'atelier
#    Je vais ajouter des commentaires explicatifs d'une part...
#    et d'autre part, je vais numeroter de maniere ordonner,
#    la progression que nous avons adopter lors de l'atelier
#    NOTE: ces sections sont commentees afin d'executer
#    l'application suivant les etapes (approx) que nous avons employees
#    au fur et a mesure que vous les decommenterai
#    Plusieurs sections peuvent etre identifiees au meme no
#    il faut donc decommenter tous les 1, puis tous les 2 et ainsi de suite
#    ATTENTION de bien aligner les espaces blancs

######### UN LOGICIEL AVEC INTERFACE GRAPHIQUE EN 13 ETAPES ###########################################
#    1- Le main -> on assure qu'on peut executer le fichier Python courant
#    2- L'import de librairies externes
#    3- Creation de la classe Controleur, et creation d'une instance
#    4- Creation de la classe Vue, creation d'une instance par et pour le Controleur
#       et initialisation de l'engin graphique avec la fonction Tk()
#       qui retourne une fenetre (placee dans self.root) qui servira de racine pour
#       tous les elements graphiques de l'application
#       NOTE on de voit toujours pas d'interface, bien que le code precedent l'ait creer
#    5- Demarrage de la boucle evenementielle de l'engin graphique
#       qui attend ces evenements pour agir...
#       NOTE maintenant on doit voir une fenetre grise de base apparaitre
#            le logiciel restera actif tant que cette fenetre ne sera pas detruite (fermee)
#    6- Ajout d'une instance de la classe Label de tkinter, directement dans la fenetre (self.root)
#       NOTE a l'execution on ne voit encore que la fenetre grise car l'instance de la classe Label
#            est cree en memoire mais pas encore affichee
#    7- en appliquant 'pack()' a l'instance, on demande au gestionnaire de geometrie (classe pack)
#       de l'afficher maintenant...
#       NOTE votre fenetre est devenu toute petite PARCE QUE les gestionnaires de geometrie
#            'shrink-wrap' le contenant autour de son contenu pour eviter la perte d'espace ...
#    8- Creation d'un contenant (classe Frame) a l'interieur de la fenetre self.root
#       c'est dans ce contenant qu'on place les widgets (window gadget, ou element graphique)
#       NOTE remarquer que le self.cadremenu s'affiche grace a 'grid' plutot que 'pack'
####### ATTENTION -> concernant les gestionnaire de geometrie
#        tkinter permet l'usage d'un seul gestionnaire de geometrie par contenant
#        AINSI tous les elements qui sont attribues a contenant doivent utiliser le meme gestionnaire
#        a votre choix, pack ou grid MAIS JAMAIS les deux dans le meme contenant
#    9- On ajoute un nouveau cadre, dans lequel on ajoute un widget de dessin, a partir de la classe Canvas
#       on utilise les variables d'instances self.largeur et self.hauteur
#       AU LIEU D'UTILISER DES VALEURS DIRECTEMENT DANS LE CODE
#    10-On ajoute un 3ieme cadre, dans lequel on place une instance de Button
#       auquel on connecte la methode redemarrer(), qui initialement ne fait qu'imprimer un texte a la console
#       on positionne self.cadreresultat avec grid, dans la deuxieme colonne, en l'etirant sur deux rangees
#       et en le dimensionnant afin qu'il colle au haut et au bas de rangees
#       On definit la methode demandee dans la classe Vue, sinon Python presenterait une erreur d'objet inconnu
#    11-On ajoute un champ permettant la saisie de texte dans le cadreresultat, en ajoutant
#       la lecture du contenu de ce champ afin de l'imprimer a la console (le second print)
#    12-On ajoute une valeur par defaut dansle champ de saisie,
#       on ajoute une condition qui test la valeur obtenue en lisant le contenut du champ (self.champ1.get())
#       (afin d'eviter les chaines vides)
#       si la condition est vraie, on appelle la methode self.dessinergeo, en fournissant 
#       la valeur qu'on transtype en entier (int())
#       On cree la methode dessinergeo(arg), pour dessiner un nombre arg de fois, un oval
#       dans sur le canevas (du dessin vectoriel)
#    13-On demande d'effacer le contenu du canevas avant d'y dessiner les prochains items...
################################################################################################################


# -2- from tkinter import *    # ceci importera les elements de cette librairie
                               # dans l'espace de nom  (namespace) du module qui l'importe
# -2- import random    # cette facon d'importer, cree un nouvel espace de nom, au nom du module
                       # dans lequel sont places ses elements, et qu'on accede par le nom complet, soit module.element()

###  ATELIER DE TKINTER DONNE LE 26 AVRIL
#    

# -4- class Vue():
    # -4- def __init__(self):
        # -4- self.root=Tk()  # Initialise l'engin graphique et 'return' la fenetre 
                        # qui servira de racine au reste des objets graphiques
                        
        # -9- self.largeur=800
        # -9- self.hauteur=600
                        
        # -8- self.cadremenu=Frame(self.root)
        ####### NOTE on doit recommenter les deux prochaines lignes avant de passer a 8
        # -6- self.etiqbonjour=Label(self.root,text="Bonjour le monde")
        # -7- self.etiqbonjour.pack(side=LEFT) #pack est le gestionnaire d'emplacement de base
                                # grid est le gestionnaire de positionnement en grille 2D
        ####################################################################################
                        
        # -8- self.etiqbonjour=Label(self.cadremenu,text="Bonjour le monde")
        # -8- self.etiqbonjour.pack(side=LEFT) #pack est le gestionnaire d'emplacement de base
                                # grid est le gestionnaire de positionnement en grille 2D
                                
        # -9- self.etiqbienvenue=Label(self.cadremenu,text="Bienvenue a notre jeu", bg="orange")
        # -9- self.etiqbienvenue.pack(side=LEFT)
        
        # -9- self.cadrejeu=Frame(self.root)
        # -9- self.canevas=Canvas(self.cadrejeu, width=self.largeur,height=self.hauteur, bg="red") # cree une surface a dessin
        # -9- self.canevas.grid(row=0,column=0) # on affiche la surface de dessin
        
        # -10- self.cadreresultat=Frame(self.root)
        # -10- self.btnredemarre=Button(self.cadreresultat, text="Redemarre",command=self.redemarrer)
        # -10- self.btnredemarre.pack(side=BOTTOM)
        
        # -11- self.champ1=Entry(self.cadreresultat,width=30)
        # -12- self.champ1.insert(0,"12")
        # -11- self.champ1.pack(side=BOTTOM)     
        
        # -8- self.cadremenu.grid(row=0, column=0)
        # -9- self.cadrejeu.grid(row=1,column=0)
        # -10- self.cadreresultat.grid(row=0, column=1,rowspan=2,sticky=N+S)
        
    # -10- def redemarrer(self):
        # -10- print("on demarre")
        # -11- valeurdechamp=self.champ1.get()
        # -11- print("on demarre",valeurdechamp)
        # -12- if valeurdechamp:
            # -12- self.dessinergeo(int(valeurdechamp))
        # -12- else:
            # -12- print("ERREUR")
        
    # -12- def dessinergeo(self,n):
        # -13- self.canevas.delete(ALL)
        # -12- for i in range(n):
            # -12- x=random.randrange(self.largeur)
            # -12- y=random.randrange(self.hauteur)
            # -12- taille=random.randrange(20)+5
            # -12- self.canevas.create_oval(x-taille,y-taille,x+taille,y+taille, fill="green")

# -3- class Controleur(): # on definit une nouvelle classe qui servira a controler la vue et le modele (absent dans l'exemple)
    # -3- def __init__(self): # on definit la methode __init__, pour initialiser l'objet cree
        # -3- pass # mot Python poiur servir de 'place holder', quelque chose mais qui fait rien...
        # -4- self.vue=Vue()
        # -5- self.vue.root.mainloop()    # demarre la boucle evenementielle
 

# -1- if __name__ == '__main__':
    # -3- moncontroleur=Controleur()

    # -1- print("Fin")