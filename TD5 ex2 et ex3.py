# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 11:03:41 2024

@author: orian
"""

from tkinter import *
import random


class Tir:
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=400, height=400, bg='red')
        self.score = 0
        ##NE PAS METTRE DE PARENTHESE A COMMANDE SINON IL L'EXECUTE DIRECT !!
        self.feu = Button(self.root, text='Feu', command = self.feuuu) #Pas de parenthèses !!
        self.quitter = Button(self.root, text = 'Quitter', command = self.root.destroy) #bouton
        
        self.canvas.grid(row =  0, column = 0) #ça me fait une grille sur la fenêtre et ca me place le canva en position (0,0)
        self.feu.grid(row = 1, column = 0, sticky = W)#ca me met le bouton sur la position (0,1). Le nb de position est infini
        self.quitter.grid(row = 1, column = 0, sticky = E)
        
        self.draw_circle(200,200, 180, 'red', 'ivory')
        self.draw_circle(200, 200, 150, 'red', 'ivory')
        self.draw_circle(200, 200, 120, 'red', 'ivory')
        self.draw_circle(200, 200, 90, 'red', 'ivory')
        self.draw_circle(200, 200, 60, 'red', 'red')
        self.draw_circle(200, 200, 30, 'red', 'ivory')
        
        self.canvas.create_line(0, 200, 400, 200, fill='red')
        self.canvas.create_line(200, 0, 200, 400, fill='red')
        
        self.canvas.create_text(200, 35,text='1', font = ('Times', '20', 'bold'),fill= 'red') #à quoi sert la fonction bold ??
        self.canvas.create_text(200, 65,text='2', font = ('Times', '20', 'bold'),fill= 'red')
        self.canvas.create_text(200, 95,text='3', font = ('Times', '20', 'bold'),fill= 'red')
        self.canvas.create_text(200, 125,text='4', font = ('Times', '20', 'bold'),fill= 'red')
        self.canvas.create_text(200, 155,text='5', font = ('Times', '20', 'bold'),fill= 'ivory')
        self.canvas.create_text(200, 185,text='6', font = ('Times', '20', 'bold'),fill= 'red')

        self.text = Text(self.root, height=1)
        self.text.grid(row = 2, column = 0)


        self.root.bind('<Key>', self.key_press)
        
        self.root.mainloop()
        
    def draw_circle(self, x, y, r, outl, fi): 
        self.canvas.create_oval(x-r, y-r, x+r, y+r, outline=outl, fill = fi )
    
    def draw_tir(self, x, y):
        self.canvas.create_oval(x-10, y-10, x+10, y+10, outline='black', fill = 'black')
        
    def feuuu(self):
        for i in range(5):
            x = random.random()*400
            y = random.random()*400
            self.draw_tir(x, y)
            self.score += self.calcul_score(x,y)
        print(self.score)
        
        self.text.delete('1.0', 'end')
        
        self.text.insert('2.0', f" Score de {self.score} point(s)")
        
        #afficher le score
    def calcul_score(self, x, y):
        position = (x-200)**2 + (y-200)**2
        if position > 34225:
            return 0
        elif position > 24025:
            return 1
        elif position > 15625:
            return 2
        elif position > 9025:
            return 3
        elif position > 4225:
            return 4
        elif position > 1225:
            return 5
        else :
            return 6
        
    def key_press(self, event):
        print('f est pressé')
        x = random.random()*400
        y = random.random()*400
        self.draw_tir(x, y)
        self.score += self.calcul_score(x,y)
        
        self.text.delete('1.0', 'end')
        
        self.text.insert('2.0', f" Score de {self.score} point(s)")
            
Tir()