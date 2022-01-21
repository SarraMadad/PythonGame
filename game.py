from email.policy import default
import pygame
import pytmx
import pyscroll

#(attributs = variables d'une classe + methodes = fonctions d'une classe)
class Game:
    #on a pas besoin d'initialiser les attributs avant le constructeur comme en java
    
    #constructeur
    def __init__(self): #self = this
        #attribut screen => creer la fenetre du jeu
        #self = objet courant dans lequel on met des trucs
        self.screen = pygame.display.set_mode((800, 600)) #taille de le fenetre
        pygame.display.set_caption("LOTR version wish") #nom du jeu
        
        #chargement des données TMX
        tmx_data = pytmx.util_pygame.load_pygame('map/basicMap.tmx')
        
        #faire la source de données pour la map
        map_data = pyscroll.data.TiledMapData(tmx_data)
        
        #on charge les différentes calques créées dans Tiled
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        
        #dessiner le groupe de caloques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
        
     
    #methodes   
    def run(self):
        #boucle du jeu : on veut garder le jeu en marche et on veut quitter le jeu proprement
        running = True #par defaut, le fenetre du jeu est active

        while running:
            #on dessine les calques sur le screen
            self.group.draw(self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #QUIT = variable = code croix
                    running = False