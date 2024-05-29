# -*- coding: utf-8 -*-
"""
Created on Wed May 29 11:38:53 2024

@author: orian
"""

import wave
import struct
import numpy as np

#exercice 1
def recup_echantillon(path):
    f = open("the_wall.wav", "rb") #IL FAUT QUE LE FICHIER the_wall SOIT DANS LE MEME DOSSIER QUE LE CODE
    data = f.read()
    
    voie1 = [] #liste contenant les echantillons de la voie 1
    voie2 = []
    
    indice = 44
    while indice < len(data):
        echantillon = struct.unpack_from("hh",data, indice)
        voie1.append(echantillon[0])
        voie2.append(echantillon[1])
        indice += 4
        
    return voie1, voie2

def recup_header():
    f = open("the_wall.wav", "rb")
    data = f.read()
    
    return data[:44]


#on a réccupéré les échantillons de chaque voie :
voie1_the_wall, voie2_the_wall = recup_echantillon("e")
header = recup_header()


def modification_echantillon(voie):#fonction qui supprime un échantillon sur 2 pour la voie donnée en attributs
    voie_modif = []
    indice = 0
    while indice < len(voie):
        voie_modif.append(voie[indice])
        indice +=2
    return voie_modif

voie1_modif = modification_echantillon(voie1_the_wall)
voie2_modif = modification_echantillon(voie2_the_wall)


def creer_ficher(header, voie1, voie2):
    with open("oriana_modif.wav","wb") as f: #si le fichier existe pas ça le créer. Ca le met en mode Writing en binaire : 'wb'
        f.write(header) #ca écrit dans le fichier 
        for i in range(len(voie1)):
            var1 = struct.pack("h",voie1[i]) #il faut restructurer la valeur de l'échantillon pour qu'elle puisse etre lue dans le fichier wav
            f.write(var1) #ca ecrit à la suite
            var2 = struct.pack("h",voie1[i])
            f.write(var2)


#Le fichier à été créé dans le même dossier que le fichier Python sous le nom 'oriana_modif"
#On peut l'écouter maintenant

creer_ficher(header, voie1_modif, voie2_modif)