import pygame
from game import Game

#
if __name__ == '__main__':

    #lancer la lib pygame
    pygame.init()

    game = Game() #on cree une variable game de type Game
    game.run() #on appelle la methode run() de la classe Game

    #ferme la fenetre
    pygame.quit() 
 