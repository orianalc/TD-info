# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 19:43:13 2024

@author: orian
"""

class Polynome:
    def __init__(self,liste_coef):
        self.liste_coef = liste_coef #list_coef est la liste des coefficients du plus petit vers le plus grand degré
               
    def __str__(self):
        str_polynome = ""
        for k in range(len(self.liste_coef)):
            if len(self.liste_coef) == 1:
                if self.liste_coef[0] == 0:
                    return "Polynôme nul"
            if k == 0:
                if self.liste_coef[0] != 0:
                    s = f"{self.liste_coef[0]}"
                    str_polynome = s + str_polynome
                    
                    
            elif k == 1:
                if self.liste_coef[1] == 0:
                    continue
                if self.liste_coef[1] == 1:
                    s = "X + "
                else :
                    s = f"{self.liste_coef[1]}*X + "
                str_polynome = s + str_polynome
            else :
                if self.liste_coef[k] == 0:
                    continue
                if self.liste_coef[k] == 1:
                    s = f"X**{k} + "
                else:
                    s = f"{self.liste_coef[k]}*X**{k} + "
                str_polynome = s + str_polynome
            
        return str_polynome
    
    
    def __add__(self,p2):
        L=[]
        n = max(len(self.liste_coef), len(p2.liste_coef))
        for k in range(n):
            if k < len(self.liste_coef) and k < len(p2.liste_coef):
                a = self.liste_coef[k] + p2.liste_coef[k]
                L.append(a)
            
            elif k < len(self.liste_coef) and k > len(p2.liste_coef)-1:
                a = self.liste_coef[k]
                L.append(a)
            
            elif k > len(self.liste_coef)-1 and k < len(p2.liste_coef):
                a = p2.liste_coef[k]
                L.append(a)
        
        return Polynome(L)
    
    def __deriv__(self):
        L=[]
        if len(self.liste_coef) == 1:
            L.append(0)
        else :
            for k in range(1,len(self.liste_coef)):
                a = self.liste_coef[k]*k
                L.append(a)
        return Polynome(L)
              
    
    def __integrate__(self,constante):
        L=[]
        L.append(constante)
        for k in range(len(self.liste_coef)):
            a = self.liste_coef[k] / (k+1)
            L.append(a)
        return Polynome(L)
    
    
#test:

P=Polynome([1,2])
print(P.__str__())

Q=Polynome([1,2,3,4,5])
L=P.__add__(Q)
print(L.__str__())
R=Q.__deriv__()
print(R.__str__())
I=Q.__integrate__(3)
print(I.__str__())