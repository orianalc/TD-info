# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 11:39:48 2024

@author: orian
"""
import matplotlib.pyplot as plt

with open("frenchssaccent.dic","r") as f:
    text = f.read() #ca fait un gros str avec un retour a la ligne marqué par \n
    words = text.split("\n") #ca devient une ligne

class Hashtable:
    def __init__(self, h, N):
        L = []
        for i in range(N):
            L.append([])
        
        self.taille = N
        self.nb_element = 0
        self.f_hachage = h
        self.table = L
    
    def put(self, key, value):
        if self.nb_element >= 1.2*self.taille:
            self.nb_element = 0
            self.resize()
            
        l_cle = [] #on crée une liste avec toutes les clés
        for i in range(len(self.table)):
            if len(self.table[i]) > 0: #on vérifie que ce soit pas une liste vide
                for k in range(len(self.table[i])):
                    l_cle.append(self.table[i][k][0]) #on rajoute la valeur des clés la premiere valeur du tuple
       
        if key not in l_cle: #on rajoute la clé
            position = self.f_hachage(key) % len(self.table)
            self.table[position].append((key,value))
            self.nb_element += 1
        
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
        
    def resize(self): #doubler la taille du tableau
        self.taille *= 2
        tab = list(self.table) # Copie de l'ancien tableau
        self.table = [[] for k in range(self.taille)]
        for l in tab: 
            for (k,v) in l:
                self.put(k,v)
        
def h_naif(chaine):
    s = 0
    for symbole in chaine:
        s += ord(symbole)
    return s
        

ht = Hashtable(h_naif, 320)
for mot in words[:int(len(words)/4)]: #Je fais moins sinon ça prend trop de temps a compiler
    ht.put(mot, len(mot))

#TROUVER LA MEILLEURE REPARTISSION :

def h_2(chaine): #methode du produit des codes ASCII
    s = 1
    for symbole in chaine:
        s += s*ord(symbole)
    return s

ht2 = Hashtable(h_2, 320)
for mot in words[:int(len(words)/4)]: #Je fais moins sinon ça prend trop de temps a compiler
    ht2.put(mot, len(mot))

ht2.affichage()


def h_3(chaine): #methode du produit des codes ASCII
    s = 1
    for symbole in chaine:
        s += s*ord(symbole)
    t = 0
    for nb in str(s):
        t += ord(nb)
    return t

ht3 = Hashtable(h_3, 320)
for mot in words[:int(len(words)/4)]: #Je fais moins sinon ça prend trop de temps a compiler
    ht3.put(mot, len(mot))

ht3.affichage()


