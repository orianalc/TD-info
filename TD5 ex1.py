# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 10:13:28 2024

@author: orian
"""
from tkinter import *

def draw_circle(x, y, r, outl, fi): #fonction pour créer un cercle à partir des ovals
    canvas.create_oval(x-r, y-r, x+r, y+r, outline=outl, fill = fi )
        
root = Tk()
canvas = Canvas(root, width=400, height=400, bg='red')
feu = Button(root, text='Feu')
quitter = Button(root, text = 'Quitter', command = root.destroy) #commande qui permet de fermer la fenêtre

canvas.grid(row =  0, column = 0) #ça me fait une grille sur la fenêtre et ca me place le canva en position (0,0)
feu.grid(row = 1, column = 0, sticky = W)#ca me met le bouton sur la position (0,1). Le nb de position est infini
quitter.grid(row = 1, column = 0, sticky = E)
#création des cercle du plus grand au plus petit parce que ça se supperpose
#il y a bien 30 pts de difference entre chaque cercle
draw_circle(200,200, 180, 'red', 'ivory' )
draw_circle(200, 200, 150, 'red', 'ivory')
draw_circle(200, 200, 120, 'red', 'ivory')
draw_circle(200, 200, 90, 'red', 'ivory')
draw_circle(200, 200, 60, 'red', 'red')
draw_circle(200, 200, 30, 'red', 'ivory')

#les lignes sont après les cercles sinon elles sont cachés
canvas.create_line(0, 200, 400, 200, fill='red')
canvas.create_line(200, 0, 200, 400, fill='red')

#les chiffres sont à la fin
canvas.create_text(200, 35,text='1', font = ('Times', '20', 'bold'),fill= 'red') #à quoi sert la fonction bold ??
canvas.create_text(200, 65,text='2', font = ('Times', '20', 'bold'),fill= 'red')
canvas.create_text(200, 95,text='3', font = ('Times', '20', 'bold'),fill= 'red')
canvas.create_text(200, 125,text='4', font = ('Times', '20', 'bold'),fill= 'red')
canvas.create_text(200, 155,text='5', font = ('Times', '20', 'bold'),fill= 'ivory')
canvas.create_text(200, 185,text='6', font = ('Times', '20', 'bold'),fill= 'red')

root.mainloop()