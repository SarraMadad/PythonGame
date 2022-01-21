import pygame
import pytmx
import pyscroll

#(attributs = variables d'une classe + methodes = fonctions d'une classe)
class Game:
    #on a pas besoin d'initialiser les attributs avant le constructeur comme en java
    
    #constructeur
    def __init__(self): #self = this
        #attribut screen => creer la fenetre du jeu
        self.screen = pygame.display.set_mode((800, 600)) #taille de le fenetre
        pygame.display.set_caption("LOTR version wish") #nom du jeu
        
        #chargement des données TMX
        tmx_data = pytmx.load_pygame('map/basicMap.tmx')
        
        #faire la source de données pour la map
        map_data = pyscroll.TiledMapData(tmx_data)
        
        #faire la couche de scroll pour déplacer la map
        screen_size = (400, 400)
        map_layer = pyscroll.BufferedRenderer(map_data, screen_size)
        
        #make the PyGame SpriteGroup with a scrolling map
        group = pyscroll.PyscrollGroup(map_layer=map_layer)
        
     
    #methodes   
    def run(self):
        #boucle du jeu : on veut garder le jeu en marche et on veut quitter le jeu proprement
        running = True #par defaut, le fenetre du jeu est active

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #QUIT = variable = code croix
                    running = False