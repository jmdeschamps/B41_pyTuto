## -*- Encoding: UTF-8 -*-  
# la ligne ci-haut doit apparaître en entête (première ligne) de votre fichier pour que python comprenne les accents

### COMMENTAIRES

# le dièse (#) sert à commenter le reste de la ligne

### QUELQUES RÈGLES

#  la casse des caractères compte   g pas égal à G


##################################################################################
# Les espaces blancs (espace, tabulation, nouvelle ligne) servent à formatter le code en bloc
#        NE JOUER PAS AVEC LES INDENTATIONS ET ESPACES EN DÉBUT DE LIGNE...
##################################################################################

### TYPES DE BASE

None # une valeur nulle, à utiliser au besoin, on en reparlera... 

2 # un entier

4.2 # un réel

"f" # caractère unique

"une chaîne de caractères" # une chaîne de ...

'une autre chaîne de caractères'  # guillemets simples ou doubles MAIS pas mélangés

""" Une
    'chaîne'
    multiligne
"""
'''
    avec 
    des
    simples
'''
## Les séquences

"ceci est une chaîne"  # chaînes de caractères (immuables)

[1,4,7,2] # une liste (crochet carré) !!!  les listes servent comme matrices, array, tableau de données

[[12,43],[8,4],[22,55]] # une liste de liste, comme un tableau à 2 dimensions maliste[1][0]

# les dictionnaires -> structure en paire clé:valeur  !!! EXTRÊMENT UTILE

{"cle1":"une valeur",
   "cle2":42,
   "cle64":[],
   101:None }

# Tuple -> comme des listes mais immuables

(12,)
(1,4,"abc",2)

### VARIABLES
# les variables n'ont pas à être déclarées mais doivent se faire assigner une valeur
# chaque variable est typée, au moment de l'assignation, par son contenu

zz=None
a="une valeur" 
b = "" # une chaîne vide
c=-2
d=4.2
d=12

### COMMANDES ET OPÉRATEURS

# Impression à la console
print("valeur",12,"autre chaîne")  #, imprime n valeurs, séparées par des virgules ','

# Lecture à la console
montexte=input("Votre texte ici s.v.p.: ")  # le texte termine lorsqu'on appuie sur la touche "Enter"

# Arithmétique:   +, -, /, *, ** (exposant)

# Transtypage
a=15.7 # a est un réel (float)
b= int(a) # b est un entier -> 15
c=str(a) # c est une chaîne -> '15.7'
d=float(c) # d est un réel -> 15.7
e=float(b) # e est un réel -> 15.0
print("TRANSTYPAGE: ",a,b,c,d,e)

# No ascii des caractères
unelettre=chr(77)
unnombre=ord("f")

# Boucle
# les boucles for fonctionne sur des séquences : dans la variable i on retrouvera la prochaine valeur de la séquence
for i in [2,5,34,78]:
    print(i)
else:
    pass # NOTE les blocs de code ne peuvent pas être vide, le mot réservé "pass" sert de jeton...

for i in range(10): # si on veut itérer un nombre n de fois, la fonction range va nous fournir cette séquence
    pass
    for j in range(10,20):
        print(i*j,i,j)

# dans l'exemple suivant le while sera vrai, donc on exécute le bloc de code
# jusqu'à ce que n==0    
n=10
while n>0:
    n-=1
    # n--  non valable en Python ni n++
    
##NOTE PAS DE UNTIL en Python

# Condition (pour l'exemple, on le met dans la boucle while)

n=10
while n>0:
    n-=1
    if n==0:
        print("n est arrivé à zéro")
    elif n==1:
        print("on y est presque")
    else:
        print(n)
    
    
### FONCTION
# mot clé 'def' -> nomdefonction(liste d'arguments,0 et plus) ':'  le double point indique
#                                                                  qu'un bloc de code suivra
def mafonction(arg1,arg2):
    print("mafonction dit: ",arg1,arg2)
    return None # ce return est ajouté implicitement si aucun return n'est défini

def autrefonction():
    print("Rien dans autre fonction")
    # ici Python ajoutera return None
    
def autrefonction2():
    print("Rien dans autre fonction2")
    return 1
    
mafonction(2,7)
autrefonction()


### CLASSE



if __name__ == '__main__':
    print("FIN")
































