# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 15:52:32 2020

@author: Justin Hoffmann

liste9 = [[6, 1], [12, 2], [8, 0], [6, 1], [8, 1], [9, 0], [5, 0], [12, 0]]
"""
liste0=[[6, 2], [12, 0], [4, 2], [1, 1], [7, 3], [0, 3], [4, 0], [3, 2]]
liste1=[[6, 0], [12, 0], [10, 1], [4, 2], [11, 2], [1, 1], [6, 3], [12, 0]]
liste2=[[8, 0], [0, 0], [9, 2], [6, 1], [7, 3], [6, 2], [2, 0], [11, 1]]
liste3=[[6, 2], [9, 1], [3, 3], [6, 2], [6, 3], [1, 1], [0, 2], [1, 0]]
liste4=[[1, 1], [0, 3], [0, 2], [5, 2], [6, 0], [0, 1], [9, 2], [2, 3]]
liste5=[[7, 2], [7, 3], [10, 2], [8, 1], [3, 3], [7, 0], [0, 0], [9, 1]]
liste6=[[1, 3], [7, 0], [0, 2], [1, 2], [11, 3], [0, 3], [1, 2], [3, 3]]
liste7=[[7, 3], [11, 3], [6, 1], [4, 0], [1, 3], [3, 0], [12, 0], [6, 3]]
liste8=[[12, 3], [12, 3], [5, 0], [11, 2], [7, 3], [10, 2], [1, 3], [2, 1]]
liste9 = [[6, 1], [12, 2], [8, 0], [6, 1], [8, 1], [9, 0], [5, 0], [12, 0]]
liste10=[[7, 3], [7, 3], [2, 0], [3, 3], [3, 0], [3, 0], [10, 0], [11, 1]]
liste11=[[6, 2], [5, 3], [0, 0], [10, 1], [5, 3], [9, 0], [8, 2], [8, 1]]
liste12=[[7, 0], [0, 3], [10, 2], [2, 3], [9, 0], [10, 0], [9, 3], [12, 0]]
liste13=[[12, 1], [7, 0], [10, 0], [9, 2], [1, 1], [8, 2], [10, 0], [8, 1]]
liste14=[[11, 3], [6, 1], [3, 3], [5, 1], [4, 3], [0, 3], [3, 0], [4, 0]]
liste15=[[1, 3], [2, 3], [7, 2], [8, 1], [9, 1], [1, 0], [11, 3], [2, 2]]
liste16=[[9, 1], [8, 2], [5, 3], [1, 3], [10, 2], [1, 1], [2, 0], [6, 1]]
liste17=[[3, 3], [12, 0], [2, 3], [0, 3], [12, 2], [5, 3], [8, 1], [0, 1]]
liste18=[[4, 0], [0, 1], [6, 1], [1, 3], [4, 2], [8, 0], [9, 1], [5, 3]]
liste19=[[7, 1], [2, 3], [2, 0], [3, 2], [0, 0], [5, 0], [5, 1], [1, 2]]




liste9 = [[6, 1], [12, 2], [8, 0], [6, 1], [8, 1], [9, 0], [5, 0], [12, 0]]

def sortByOccurence(liste):

    listeRetour = []
            
    for x in range(8) :
        sousListe = liste[x]
        ValeurDeSousListe = sousListe[0]
        compteur = 0
        for y in range(8):
            sousListeDeComparaison = liste[y]
            ValeurDeSousListeDeComparaison = sousListeDeComparaison[0]
            if(ValeurDeSousListe == ValeurDeSousListeDeComparaison):
                compteur = compteur+1
        if(compteur>1):
            present = 0
            listePourListeRetour =[ValeurDeSousListe,compteur]
            for l in range(len(listeRetour)):
                souslisteDeListeRetour = listeRetour[l]
                if(listePourListeRetour == souslisteDeListeRetour):
                    present = 1
            if(present==0):
                inc=0
                for i in range(len(listeRetour)):
                    souslisteDeListeRetour = listeRetour[i]
                    if(souslisteDeListeRetour[0]>ValeurDeSousListe):
                        inc=+1
                listeRetour.insert(inc,listePourListeRetour) 
                
    print("Input matrix : ", liste)
    
    print("Paire output :",listeRetour)
    print(" ")
    

sortByOccurence(liste0)
sortByOccurence(liste1)
sortByOccurence(liste2)
sortByOccurence(liste3)
sortByOccurence(liste4)
sortByOccurence(liste5)
sortByOccurence(liste6)
sortByOccurence(liste7)
sortByOccurence(liste8)
sortByOccurence(liste9)
sortByOccurence(liste10)
sortByOccurence(liste11)
sortByOccurence(liste12)
sortByOccurence(liste13)
sortByOccurence(liste14)
sortByOccurence(liste15)
sortByOccurence(liste16)
sortByOccurence(liste17)
sortByOccurence(liste18)
sortByOccurence(liste19)


                
            
                
                
            
            
            
            
            