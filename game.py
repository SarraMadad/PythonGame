import pygame
import pytmx
import pyscroll

#(attributs + methodes)
class Game:
    
    #constructeur
    def __init__(self): #self = this
        #creer la fenetre du jeu
        pygame.display.set_mode((800, 600)) #taille de le fenetre
        pygame.display.set_caption("LOTR version wish") #nom du jeu
     
    #methodes   
    def run(self):
        #boucle du jeu : on veut quitter le jeu proprement
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #QUIT = variable = code croix
                    running = False