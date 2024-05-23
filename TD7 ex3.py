# -*- coding: utf-8 -*-
"""
Created on Wed May 22 12:47:12 2024

@author: orian
"""

from tkinter import *
import numpy as np
import random


"""
Pour retrouver les deux composantes connexes du graphe, il suffit de faire
apparaitre chaque sommet en la couleur qui lui est attribué par tab_color.
Donc tous les sommets avec la valeur 0 seront de la même couleur, ect ...

Pour cela je définie une nouvelle fonction : connexe
qui calcul le tab_color et ensuite je retrace les couleurs du graphe 
grace à la touche f.
"""

class Graph:
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=600, height=500)
        
        self.color = ['antiquewhite', 'aqua', 'aquamarine',  'bisque', 'black',  'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgrey', 'darkgreen', 'darkkhaki', 'darkmagenta', 'darkolivegreen']
        self.graph = [[2, 7], [3], [5, 8], [10], [3, 1], [], [3, 10, 4], [], [], [10, 1], [3, 1], [0]]

        self.tab_color = [i for i in range(len(self.graph))]        

        self.pos = ([131, 352], [464, 315], [254, 211], [393, 346], [381, 432], [343,  98], [298, 326], [187, 475], [245, 407], [483, 212], [365, 216], [149, 198])

       
        self.canvas.grid(row =  0, column = 0) #ça me fait une grille sur la fenêtre et ca me place le canva en position (0,0)

        for i in range(len(self.graph)):
            for j in self.graph[i]:  # sucs de i a j
                self.canvas.create_line(self.pos[i][0], self.pos[i][1],self.pos[j][0], self.pos[j][1])
        
        for i in range(len(self.graph)):
            (x,y) = self.pos[i]
            self.canvas.create_oval(x-10,y-10,x+10,y+10, fill= self.color[i])
               
      
        for i in range(len(self.graph)): #i = numéro du sommet
            self.canvas.create_text(self.pos[i][0], self.pos[i][1],text=f'{i}', font = ('Times', '12', 'bold'),fill= 'black')
        
        self.root.bind('<Key>', self.key_press)
        
        self.root.mainloop()
    
    """
    quand on a un sommet i, si le plus petit sommet adjencent à i vaut 2, alors i et tous ses vosins valent i.
    ce qui vaut i cest tab_color[i] = 2 (et c'est voisin)
    2 est lentier écrit sur le sommet
    """
    def min_local(self, i, graph, tab_color):
        #on vérifie les sommets sucs qui sont dans le graph à la position i 
        sucs_sommet = self.graph[i]
        vmin = tab_color[i]
        if sucs_sommet == []:
            vmin = tab_color[i]
        else:
            for s in sucs_sommet:
                if tab_color[s] < vmin:
                    vmin = tab_color[s]
        #on vérifie mtn si i n'est pas le successeur d'un autre sommet
        for j in range(len(graph)):
            if i in graph[j]:
                if tab_color[j] < vmin:
                    vmin = tab_color[j]
                    
        # Ensuite on change la valeur de tab_color du sommet i et de ses voisins       
        tab_color[i] = vmin
        
        if len(sucs_sommet) != 0:
            for s in sucs_sommet:
                tab_color[s] = vmin  
                    
        for j in range(len(graph)):
            if i in graph[j]:
                tab_color[j] = vmin
        
    
    def key_press(self, event):
        print('le graphe devient coloré selon ses parties connexes')
        
        #on modifie tab_color
        self.canvas.delete("all")
        
        for i in range(len(self.graph)):
            self.min_local(i, self.graph, self.tab_color)
        
        for i in range(len(self.graph)):
            self.min_local(i, self.graph, self.tab_color)
      
        
        #on modifie le graphe
        for i in range(len(self.graph)):
            for j in self.graph[i]:
                self.canvas.create_line(self.pos[i][0], self.pos[i][1], self.pos[j][0], self.pos[j][1])
        
        for i in range(len(self.graph)):
            (x,y) = self.pos[i]
            self.canvas.create_oval(x-10,y-10,x+10,y+10, fill= self.color[self.tab_color[i]])
           
        for i in range(len(self.graph)):
            self.canvas.create_text(self.pos[i][0], self.pos[i][1], text=f'{i}', font=('Times', '12', 'bold'), fill='black')

        
A = Graph()