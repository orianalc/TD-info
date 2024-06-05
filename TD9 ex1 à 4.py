# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 12:56:55 2024

@author: orian
"""


class PolynomeZq:
    def __init__(self, coef, q, n):
        if not len(coef) == 5:
            raise AssertionError("La liste de coefficient n'a pas la bonne taille")
        if not n >= 5:
            raise AssertionError("Changez la valeur de n")
        for i in coef:
            if not i < q:
                raise AssertionError(f"le coef {i} n'est pas compatible avec q. \n Rentrez des valeurs entre 0 (compris) et q (exclu).")
       
                
        self.q = q
        self.n = n
        
        self.coef = coef
     
    def __add__(self, p2):
        if not self.q == p2.q :
            raise AssertionError("Les deux polynomes n'ont pas les mêmes q")
        if not self.n == p2.n :
            raise AssertionError("Les deux polynomes n'ont pas les mêmes n")
        
        coef = [0 for i in range(len(self.coef))]
        for i in range(len(self.coef)) :
            coef[i] = self.coef[i] + p2.coef[i]
            
        #on corrige les valeurs de coef pour être sur que c'est inférieur à q
        for i in range(len(coef)) :
            val = coef[i]
            if not val < self.q:
                coef[i] = val%self.q
                
        return PolynomeZq(coef, self.q, self.n)
    
    
    def __mul__(self, p2):
        if not self.q == p2.q :
            raise AssertionError("Les deux polynomes n'ont pas les mêmes q")
        if not self.n == p2.n :
            raise AssertionError("Les deux polynomes n'ont pas les mêmes n")
        
        coef = [0 for i in range(len(self.coef))]
        
        for i in range(len(self.coef)):
            for j in range(len(self.coef)):
                m = self.coef[i]*p2.coef[j]
                if i+j > 4:#car la longeur de la liste de l'attribut coef est 5
                    p = i+j - self.n
                    coef[p] -= m
                    
                else:
                    coef[i+j] += m
        #modulo q à la fin
        for i in range(len(self.coef)):
            val = coef[i]
            coef[i] = val % self.q
        
        return PolynomeZq(coef, self.q, self.n )
                
    
    def scalar(self,c):
        for i in range(len(self.coef)):
            val = self.coef[i]
            self.coef[i] = (val*c) % self.q
            
    def rescale(self, r):
        """
        La fonction rescale transpose juste les coefficients en changeant self.q
        Il faut juste ensuite appliquer un nouveau modulo r.
        On modifie directement le polynome, pas besoin d'un return PolynomeZq(coef,self.q,self.n)
        contrairement aux fonctions add et mul.
        """
        self.q = r
        for i in range(len(self.coef)):
            val = self.coef[i]
            self.coef[i] = val % self.q
            
    def fscalar(self, r, alpha):
        """
        La fonction recalculer les valeurs des coefficients du polynome en fonction
        de r et alpha. Mais les valeurs self.n et self.q ne changent pas.
        Il faut juste ensuite appliquer le modulo q pour être sûr que les valeurs 
        ne dépassent pas q.
        On modifie directement le polynome, pas besoin d'un return PolynomeZq(coef,self.q,self.n)
        contrairement aux fonctions add et mul.
        """
        for i in range(len(self.coef)):
            val = round(self.coef[i]*alpha)
            self.coef[i] = val%r
        
        for i in range(len(self.coef)):
            val = self.coef[i]
            self.coef[i] = val % self.q
            
A = PolynomeZq([4,2,5,5,6], 10, 5)
B = PolynomeZq([0,0,0,0,0], 10, 5)
C = A.__add__(B)
print("Les coefficients du polynome C sont :")
print(C.coef)

AA = PolynomeZq([0, 0, 0, 4, 5], 10, 5)
BB = PolynomeZq([0, 0, 2, 0, 0], 10, 5)
CC = AA.__mul__(BB)
print("\n")
print("Les coefficients du polynome CC sont :")
print(CC.coef)