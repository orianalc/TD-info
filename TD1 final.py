# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 12:50:16 2024

@author: orian
"""
#TIRAGE TEST
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','-']
l1 = ['i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','-']
l2 = ['a','b','c','d','e','f','n','o','p','q','r','s','t','u','v','w','x','y','z','-']
# l3 = alphabet sans tiret 
l3 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
l4 = ['a','h','i','j','k','l','m','n','o','p','q','r','s','y','z','-']



mots_possiblestest = []
f=open("mots.txt",'r')
for ligne in f:
    mots_possiblestest.append(ligne[0:-1])


points = {'a' : 1,'b' : 3,'c' : 3,'d' : 2,'e' : 1,'f' : 4,'g' : 2,'h' : 4,'i' : 1,'j' : 8,'k' : 10,'l' : 1,'m' : 2,'n' : 1,'o' : 1,'p' : 3,'q' : 8,'r' : 1,'s' : 1,'t' : 1,'u' : 1,'v' : 4,'w' : 10,'x' : 10,'y' : 10,'z' : 10, '-' : 0, '?' : 0}
#sachant que le tiret vaut 0 point.

def score(mot):
    score_mot = 0
    for lettre in mot:
        score_mot += points[lettre]
    return score_mot

def max_score(liste_mot):
    b = 0 
    for mot in liste_mot:
        if b < score(mot):
            a = mot
            b = score(mot)
    return (a,b)

def scrable(mots_possibles,tirage):
    liste_mot = []
    for i in mots_possibles:
        t = tirage.copy()   #faire une copie sinoooon ca modifie tout tout le temps !!!!
        verification = "non"          #on réinitialise la vérification
        for j in i:
            if j in t :     #attention a bien utiliser la copie !!!!!
                verification = "oui"
                t.remove(j)
                continue
            else:
                if '?' in t :  #si la lettre n'est pas dans le tirage on regarde si on a un joker.
                    verification = "oui"
                    t.remove('?')
                    continue
                else:
                    verification = "non" #ca veut dire que toutes les lettres sont aaccepté
                    break
        if verification == "oui":
            liste_mot.append(i)
    return(max_score(liste_mot))
