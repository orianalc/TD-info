# -*- coding: utf-8 -*-
"""
Created on Sun May 19 19:23:46 2024

@author: orian
"""

from tkinter import *
import numpy as np
import random

class Graph:
    def __init__(self):
        self.root = Tk()
        self.canvas_width = 1000
        self.canvas_height = 800
        self.canvas = Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.centre = np.array([self.canvas_width / 2, self.canvas_height / 2])
        self.graph = [[2, 7, 3], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6, 0], 
                      [3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9]]
        
        self.pos = np.array([(random.randint(50, 750), random.randint(50, 550))
                             for i in range(len(self.graph))], dtype=float) #on enleve les pixels trop au bords 
        self.vitesses = np.zeros_like(self.pos)  # initialisation des vecteurs vitesses
        
        self.canvas.grid(row=0, column=0)

        self.draw_graph()
        
        self.root.bind('<Key>', self.key_press)
        self.root.mainloop()

    def draw_graph(self):
        self.canvas.delete("all")
        
        for i in range(len(self.graph)):
            for j in self.graph[i]:
                self.canvas.create_line(self.pos[i][0], self.pos[i][1], self.pos[j][0], self.pos[j][1])
        
        for (x, y) in self.pos:
            self.canvas.create_oval(x-15, y-15, x+15, y+15, fill="#f3e1d4")
        
        for i in range(len(self.graph)):
            self.canvas.create_text(self.pos[i][0], self.pos[i][1], text=f'{i}', font=('Times', '12', 'bold'), fill='black')

    def key_press(self, event):
        if event.char == 'f':
            print('f est pressé')
            forces = np.zeros((len(self.graph), 2), dtype=float)
            
            # calcul des forces de ressort entre les sommets connectés
            for i in range(len(self.graph)):
                for j in self.graph[i]:
                    force = self.calcul_force(self.pos[i], self.pos[j])
                    forces[i] += force  # Ajouter la force au sommet i
                    forces[j] -= force  # Ajouter la force opposée au sommet j
            
            # calcul de la force qui rapproche les sommets du centre du canvas
            barycentre = self.calcul_barycentre(self.pos)
            force_centre = self.calcul_force(barycentre, self.centre) * len(self.graph)
            for i in range(len(self.graph)):
                forces[i] += force_centre  # appliquer la force qui recentre à chaque sommet
            
            # on met à jour les vecteurs vitesses suite à la force centrifuge
            self.vitesses += forces * 0.1  
            self.pos += self.vitesses  
            
            self.draw_graph()
    
    def calcul_barycentre(self, pos):
        return np.mean(pos, axis=0)
    
    def calcul_force(self, posA, posB):
        k = 0.01  
        l0 = 150  
        vecteur = posB - posA 
        distance = np.linalg.norm(vecteur)  
        force_norme = k * (distance - l0)  # norme de la force
        force_direction = vecteur / distance if distance != 0 else np.zeros_like(vecteur)  # direction de la force
        return force_norme * force_direction  

Graph()
