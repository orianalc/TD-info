# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:19:11 2024

@author: orian
"""

#IMPORT PGCD
from math import gcd

class Fraction :
     def __init__(self,a,b):#ca permet d'initilaliser les valeurs direct grace a (1)
            assert b != 0
            self.numerateur = int(a)
            self.denominateur = int(b)
     
     def __str__(self):#ca permet d'afficher le vecteur des qu'il est appelé
         return f"({self.numerateur}/{self.denominateur})"
     
     def __add__(self, other):
         if self.denominateur == other.denominateur :
             a = self.numerateur + other.numerateur
             b = self.denominateur
         else:
             a = self.numerateur*other.denominateur + other.numerateur*self.denominateur
             b = self.denominateur*other.denominateur
         return Fraction(a,b) 
     
     def __mult__(self,other):
         a = self.numerateur*other.numerateur
         b = self.denominateur*other.denominateur
         return Fraction(a,b)
     
     def __simplify__(self): 
         a = self.numerateur//gcd(self.numerateur,self.denominateur)
         b = self.denominateur//gcd(self.numerateur,self.denominateur)
# par défault on crée un nvx objet plutot que modifier le deja existant.
         return Fraction(a,b)
     
        
       ### EXERCICE 3 ###
def H(n):
    s = Fraction(0,1)
    for indice in range(1, n+1):
        s = s.__add__(Fraction(1,indice))
    return s.__simplify__()

#on trouve que H(10000) vaut environ : 9.787606036044382



       ### EXERCICE 4 ###
def leibniz(n):
    s = Fraction(0,1)
    for k in range(n+1):
        s = s.__add__(Fraction((-1)**k,2*k + 1))
    return s.__simplify__()
       
#on trouve que leibniz(10000) vaut environ : 0.7854231608976358
       