# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 10:00:48 2024

@author: orian
"""

import matplotlib.pyplot as plt

class Hashtable:
    def __init__(self, h, N):
        L = []
        for i in range(N):
            L.append([])
            
        self.f_hachage = h
        self.table = L
    
    def put(self, key, value):
        l_cle = [] #on crée une liste avec toutes les clés
        for i in range(len(self.table)):
            if len(self.table[i]) > 0: #on vérifie que ce soit pas une liste vide
                for k in range(len(self.table[i])):
                    l_cle.append(self.table[i][k][0]) #on rajoute la valeur des clés la premiere valeur du tuple
       
        if key not in l_cle: #on rajoute la clé
            position = self.f_hachage(key) % len(self.table)
            self.table[position].append((key,value))
        
        else:
            position = self.f_hachage(key) % len(self.table)
            for indice in range(len(self.table[position])): #pour chaque élément de la case
                if self.table[position][indice][0] == key: #on regarde la premier valeur de chaque tuple de chaque liste contenue dans la case
                    self.table[position][indice] = (key, value) #On remplace par un nouveau tuple
    
    
    def get(self,key):
        for i in range(len(self.table)):
            if len(self.table[i]) > 0: #on vérifie que ce soit pas une liste vide
                for k in range(len(self.table[i])):
                    if self.table[i][k][0] == key:
                        return self.table[i][k][1]
        return None
        
    def affichage(self):
        x = [i for i in range(len(self.table))]
        y = []
        for case in self.table:
            y.append(len(case))
            
        width = 1/1.5
        plt.bar(x, y, width, color="blue")
        plt.show()
            
        
        
        
def h_naif(chaine):
    s = 0
    for symbole in chaine:
        s += ord(symbole)
    return s



       
        
        
#TEST METHODE PUT                

test = Hashtable(h_naif, 10)

test.put('abc',3)
print("Apres avoir ajouté une clé la table de notre objet est :")
print(test.table) 
print('\n')
test.put('abc',14)
print("Vérification du changement de valeur de la clé 'abc':")
print(test.table) 
print('\n')
             
#TEST METHODE GET
print("Sortie de la commande test.get('abc') :")
print(test.get('abc'))
print('\n')
print("Sortie de la commande test.get('aaa') :")
print(test.get('aaa'))

#TEST AFFICHAGE 
test.put('aacc',13)
test.put('abba',10)
test.put('ggº',100)
test.affichage()


"""
POUR PUT :
    ne pas faire linear probing (c'est a dire ne pas augmenter N')
    
Il faut faire Separate chaining !!
C'est a dire que chaque case contient une liste plutot qu'un tuple simple.
LA POSITION DANS LA LISTE COMPTE DU COUP !!!

Pour savoir a quelle position de la liste on met la clé et la valeur il faut
utiliser la fonction de hachage self.f_hachage.

On calcule f_hachage(cle) modulo la longueur de table (N) et on le met dans 
la case correspondante.

EXEMPLE : 
    h(‘a’) % 6 = 3 donc (‘a’, 12)  va à la 3eme place de la liste
    h(‘ab’) % 6 = 4 donc (‘ab’, 17)  va à la 3eme place de la liste
    
    si h(‘abc’) % 6 = 3 
    alors la case 3 passe de [(‘a’, 12)] à [(‘abc’,42), (‘a’, 12)]
"""
    