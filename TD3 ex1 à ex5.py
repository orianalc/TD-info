# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 15:12:14 2024

@author: orian
"""

#EXERCICE 2

class Tree:
    def __init__(self,label,*children): #* veut dire que on peut mettre un nb infini d'element qui correspondront a l'attribut children, children peut aussi etre vide !!!
        self.__label = label
        self.__children = children # !!! il faut enlever l'étoile et par défault ca devient un tuple
        
    def label(self):
        return self.__label
    
    def children(self):
        return tuple(self.__children)
      
    def nb_children(self):
        return len(self.__children)

    def child(self,i):    # i = 0 (fils de gauche) ou i = 1 (fils de droite)
        if not i+1 <= self.nb_children() :
            raise AssertionError("L'arbre ne possède pas assez de Children")
        return self.__children[i]
        
    def is_leaf(self):
        if self.nb_children() == 0:
            return True
        else :
            return False
    
    def depth(self):
        if self.is_leaf() == True:
            return 0
        else :
            if self.nb_children() == 2:
                m = 1 + max(self.__children[0].depth(), self.__children[1].depth())
                return(m)
            else:
                m = 1 + (self.__children[0].depth())
                return(m)
         
    def __str__(self):
        #Je ne travaille qu'avec des arbres binaires
        if self.nb_children() == 0:
            return f"{self.__label}"
        else :
            if self.nb_children() == 2:
                return f"{self.__label}({self.__children[0].__str__()},{self.__children[1].__str__()})"
            else :
                return f"{self.__label}({self.__children[0].__str__()})"
      
    def __eq__(self,autre_arbre): #
        if self.is_leaf() and autre_arbre.is_leaf():
                if self.__label == autre_arbre.__label:
                    return True
                else :
                    return False
        elif self.nb_children() == autre_arbre.nb_children():
            for i in range(self.nb_children()):
                if not self.child(i).__eq__(autre_arbre.child(i)):
                    return False
            return True
        else :
            return False
        
        
    #On considère que les arbres binaires strict. (soit 2 ou a)
    #On se résume donc aux opérations + - / * et non exp, sin, cos qui eux aurait eu besoin que d'un seul fils pour les représenter
    
    def deriv(self, var): 
        #cas feuille seul
        if self.is_leaf(): #2 cas possibles  (cte OU var)
             if self.__label == var:
                 return Tree('1')
             else :
                 return Tree('0')
        elif self.__label == '+':
            return Tree('+',
                        self.child(0).deriv(var),
                        self.child(1).deriv(var)
                        )
        elif self.__label == "*":
            return Tree('+',
                       Tree('*', self.child(0).deriv(var), self.child(1)),
                       Tree('*',self.child(0), self.child(1).deriv(var))
                       )
            
        
        
T = Tree('f', Tree('a'),Tree('b'))
T3 = Tree('vide')
TT3 = Tree('vide')
T4 = Tree('test',T,Tree('ee', Tree('c')))
T5 =  Tree('testdepth',T4,T)

print('test str')
print(T4.__str__())
print(T5.__str__())
print(T.__str__())
print("\n")

print('test is_leaf')
print(T4.is_leaf())
print(T5.is_leaf())
print(T3.is_leaf())
print("\n")

print('test nb_children')
print(T4.nb_children())
print(T5.nb_children())
print(T.nb_children())
print("\n")

print('test child')
print(T4.child(0).__str__())
print(T4.child(1).__str__())
print(T5.child(0).__str__())
print("\n")

print("test depth :")
print(T4.depth())
print(T5.depth())
print(T.depth())
print("\n")

print('test __eq__')
print(T4.__eq__(T4))
print(T5.__eq__(T4))
print(T5.__eq__(T5))
print("\n")

print('test deriv')
TD = Tree('+',Tree('a'),Tree('b'))
print(TD.deriv('b').__str__())
TD2 = TD = Tree('*',Tree('a'),TD)
print(TD2.deriv('b').__str__())