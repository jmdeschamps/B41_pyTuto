## -*- Encoding: UTF-8 -*-  

########## Python est Orienté Objet ########################################################################
# Tout est un objet pour Python
#        les programmes
#        les modules
#        les fonctions
#        les types de base
#        les classes
#    et naturellement
#        les instances que vous créez à partir de ces classes
##################################################################################

###  ATTENTION -> Python n'est PAS Java  (je réfère à l'excellent Java
#                 car je crois c'est là que la plupart avez eu votre introduction
#
#                A priori TOUT est public en Python
#                donc pas de public, private, protected
#
#                Python permet de mettre autant de choses qu'il vous plaira dans un même fichier
#                Pas de liens entre le nom de fichier et son contenu
#
#                SVP ne créé pas un fichier par classe, à moins que cela ait un sens !!!!!!
#
#    j'utilise le mot "méthode" pour référer aux fonctions définit DANS une classe
#    J'utilise le mot "objet" pour parler généralement des instances
#    J'utilise le mot "instance" pour parler d'un objet particulier d'une classe

### PRINCIPES OOP en Python (avec exemple de syntaxe de base)
# exemple 1
class Mapremiereclasse(): # le consensus de la communauté Python est de nommer les classes en débutant avec une majuscule
    def __init__(self,age): # méthode d'initialisation de l'instance
        self.monage=age
        return None         # ATTENTION init doit retourner None mais le fait pas défaut donc pas de return requis
        
    def autremethode(self):
        print("Mon age est de:",self.monage)
        
monpremierobjet=Mapremiereclasse(100) # demande la création d'uns instance avec un argument qui est passé à la méthode "__init__"

# DONC        
# On définit des classes, desquelles on demandera la génération d'instances
#    class Mapremiereclasse():

# On définit ce qu'un objet fera lors de sa création dans une méthode SPÉCIALE "__init__(self,args)"
#        def __init__(self,age): 

# la méthode "__init__" prends le rôle du ou des constructeurs en Java (ou C++, C#, etc)
#     self.monage=age  indique que l'objet qui vient d'être créé disposera maintenant d'une variable d'instance "age" (un attribut)

# la fonction "__init__" est appelée AUTOMATIQUEMENT par Python lorsqu'on demande la création d'une instance
# NOTE: c'est là qu'on définit les attributs dont les objets disposeront

# ATTENTION SPÉCIALE -> Python crée l'objet AVANT  d'exécuter la fonction "__init__"
#                       Pour ce faire, la définition des classes utilise le mot "self"
#                       comme variable de l'objet qui vient d'être créé.
#                       "self" DOIT être le premier argument de TOUTES les méthodes, pour que Python y affecte l'objet créé.
#                       Lors des appels de méthodes, on ne tient pas compte du self (on n'a pas à y mettre quoi que ce soit)
#                       puisque Python y mettra la référence à l'objet lui même.........
#
#                       Python est "TRÈS" dynamique, permet l'ajout d'attributs à un objet à n'importe quel moment
#                       CEPENDANT - tous les attributs dont un objet aura besoin DEVRAIENT être définis dans "__init__"

# les instances d'une classe sont des objets, créées en invoquant la classe avec les arguments initiaux (s'il y a lieu)
# NOTE: Python n'utilise PAS le mot "new" pour créer un objet

# Python dispose, parfois à sa façon, des principes habituels de la programmation orientée objet: heritage, encapsulation, surcharge ds opérateurs,
# surcharge ds fonctions, etc

# ATTENTION -> KISS (Keep It Simple and Smart - oui il y a d'autres variantes ;-) ) On garde ça simple
#              pas besoin d'appliquer ces principes pour le projet courant
#              l'usage de base des objets sera suffisant



if __name__ == '__main__':
    print("J'imprime ma classe: ", Mapremiereclasse, " <- indique que la classe appartient à l'espace de nom '__main__'")
    print("J'imprime mon instance: ", monpremierobjet, " <- indique que l'objet est une instance de la classe Mapremiereclasse et se trouve à l'adresse indiquée en mémoire")
    print("J'imprime un attribut de l'instance: ", monpremierobjet.monage)
    print("On dit à l'instance d'exécuter cette méthode: ", monpremierobjet.autremethode())
    print("FIN")













 


















