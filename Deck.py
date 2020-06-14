# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 14:59:11 2020

@author: Leonard Rivals
"""

"""
Tu crees une class Deck()
qui simule un parquet de cartes
avec les methodes suivante :
Deal distribution de carte
Transfer transfer des cartes in_deck a in_game et inversement
fonction _str_, et _del_ bien sure
et un reset pour reset le packet
"""
from random import *

class Deck():
    
    
    def ___init___():
        pioche = []
        couleurs = ['Coeur', 'Carreau', 'Pique', 'Trèfle']
        for each in couleurs:
            for i in range(1,14):
                carte = [i,each]
                pioche.append(carte)
        #print(pioche)
                
        def shuffle(pioche):
            piocheMelange=[]
            for i in range (0, 52):
                index = randrange(0, 52-i)
                piocheMelange.append(pioche[index])
                del pioche[index]
            return piocheMelange
        
        pioche = shuffle(pioche)
        return pioche
    
        
    def ___str___(deck):
        
        def strHelp(val):
            if(val==1):
                return 'As'
            elif ( val >10):
                if (val==11):
                    return 'Valet'
                elif( val==12):
                    return 'Dame'
                elif(val==13):
                    return'Roi'
            else:
                return val
            
        print('Le deck est composé de :')
        str =''
        for i in range(len(deck)):
            carte = deck[i]
            str = strHelp(carte[0]) , ' de ',carte[1],   
            print(str)
        
    
    
    
    def ___del___(deck):
        deck = []
        return deck
            
    
    
    def Deal(pioche, joueur) :
        if(joueur == True):
            deckJoueur = []
            for i in range(2):
                deckJoueur.append(pioche[0])
                del pioche[0]
            return deckJoueur
        else:
            deckDeJeu=[]
            for i in range(5):
                deckDeJeu.append(pioche[0])
                del pioche[0]
            return deckDeJeu
            
    
    def transferDansLaMain(indeck , ingame, index):
        indeck.append(ingame[index])
        del ingame[index]
        
    def transferDansLeDeck(indeck , ingame, index):
        ingame.append(indeck[index])
        del indeck[index]
    
    pioche = ___init___()
    print(pioche)
    
    joueur1 = True
    deckTest = Deal(pioche, joueur1 )
    ___str___(deckTest)
    
    print(pioche)
