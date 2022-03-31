#Créé le 10/03/2022 à 12:35 CET
#Créé par Anthony Presman
#Projet: Jeu du cavalier

from random import *
# Importation de pygame
from pygame.locals import *
import pygame
pygame.init()

# Initialisation de la fenetre
largeur = 800
hauteur = 800
windowSurface = pygame.display.set_mode((largeur, hauteur), 0,32)
bouse = pygame.image.load("bouse.gif")
cavalier = pygame.image.load("cavalier.gif")

compteur = 0

#Variable de la position courrante du cavalier
cx = 0
cy = 0

# Initialisation des parametres
BLCK = 0, 0, 0
WHITE = 255, 255, 255
C = BLCK

def start_pos ():
    x = randint(0,7) * 100
    y = randint(0,7) * 100
    return x,y
start = start_pos()
current_pos = (start)
(cx, cy) = (start)
current_pos = (cx, cy)

GRILLE = [
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0]
           ]

current_pos = (start)
windowSurface.blit(cavalier, (start))
(cx, cy) = (start)
gri_pos_x = round(cx / 100)
gri_pos_y = round(cy / 100)
GRILLE[gri_pos_y] [gri_pos_x] = 1

pygame.display.flip()

#Positions disponibles
AVA = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]

# Boucle de jeu
clock = pygame.time.Clock()
running = True
while running:
    # Limitation du nombre de tours de boucle par seconde
    clock.tick(10)
    # Boucle des evennements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Elements a tracer

    #Affichage des carrés blancs:
    pygame.draw.rect(windowSurface,WHITE, (700, 000, 100, 100),)
    pygame.draw.rect(windowSurface,WHITE, (700, 600, 100, 100),)
    pygame.draw.rect(windowSurface,WHITE, (700, 400, 100, 100),)
    pygame.draw.rect(windowSurface,WHITE, (700, 200, 100, 100),)

    pygame.draw.rect(windowSurface,WHITE, (600, 700, 100, 100),)
    pygame.draw.rect(windowSurface,WHITE, (600, 500, 100, 100),)
    pygame.draw.rect(windowSurface,WHITE, (600, 300, 100, 100),)
    pygame.draw.rect(windowSurface,WHITE, (600, 100, 100, 100),)

    pygame.draw.rect(windowSurface,WHITE, (500, 000, 100, 100),)
    pygame.draw.rect(windowSurface,WHITE, (500, 600, 100, 100),)
    pygame.draw.rect(windowSurface,WHITE, (500, 400, 100, 100),)
    pygame.draw.rect(windowSurface,WHITE, (500, 200, 100, 100),)

    pygame.draw.rect(windowSurface,WHITE, (400, 700, 100, 100),)
    pygame.draw.rect(windowSurface,WHITE, (400, 500, 100, 100),)
    pygame.draw.rect(windowSurface,WHITE, (400, 300, 100, 100),)
    pygame.draw.rect(windowSurface,WHITE, (400, 100, 100, 100),)

    pygame.draw.rect(windowSurface,WHITE, (300, 000, 100, 100),)
    pygame.draw.rect(windowSurface,WHITE, (300, 600, 100, 100),)
    pygame.draw.rect(windowSurface,WHITE, (300, 400, 100, 100),)
    pygame.draw.rect(windowSurface,WHITE, (300, 200, 100, 100),)

    pygame.draw.rect(windowSurface,WHITE, (200, 700, 100, 100),)
    pygame.draw.rect(windowSurface,WHITE, (200, 500, 100, 100),)
    pygame.draw.rect(windowSurface,WHITE, (200, 300, 100, 100),)
    pygame.draw.rect(windowSurface,WHITE, (200, 100, 100, 100),)

    pygame.draw.rect(windowSurface,WHITE, (100, 000, 100, 100),)
    pygame.draw.rect(windowSurface,WHITE, (100, 600, 100, 100),)
    pygame.draw.rect(windowSurface,WHITE, (100, 400, 100, 100),)
    pygame.draw.rect(windowSurface,WHITE, (100, 200, 100, 100),)

    pygame.draw.rect(windowSurface,WHITE, (000, 700, 100, 100),)
    pygame.draw.rect(windowSurface,WHITE, (000, 500, 100, 100),)
    pygame.draw.rect(windowSurface,WHITE, (000, 300, 100, 100),)
    pygame.draw.rect(windowSurface,WHITE, (000, 100, 100, 100),)

    #Tracer les carrés noirs
    pygame.draw.rect(windowSurface,C, (600, 00, 100, 100),)
    pygame.draw.rect(windowSurface,C, (600, 600, 100, 100),)
    pygame.draw.rect(windowSurface,C, (600, 400, 100, 100),)
    pygame.draw.rect(windowSurface,C, (600, 200, 100, 100),)

    pygame.draw.rect(windowSurface,C, (500, 100, 100, 100),)
    pygame.draw.rect(windowSurface,C, (500, 700, 100, 100),)
    pygame.draw.rect(windowSurface,C, (500, 500, 100, 100),)
    pygame.draw.rect(windowSurface,C, (500, 300, 100, 100),)

    pygame.draw.rect(windowSurface,C, (700, 100, 100, 100),)
    pygame.draw.rect(windowSurface,C, (700, 700, 100, 100),)
    pygame.draw.rect(windowSurface,C, (700, 500, 100, 100),)
    pygame.draw.rect(windowSurface,C, (700, 300, 100, 100),)

    pygame.draw.rect(windowSurface,C, (400, 00, 100, 100),)
    pygame.draw.rect(windowSurface,C, (400, 600, 100, 100),)
    pygame.draw.rect(windowSurface,C, (400, 400, 100, 100),)
    pygame.draw.rect(windowSurface,C, (400, 200, 100, 100),)

    pygame.draw.rect(windowSurface,C, (300, 100, 100, 100),)
    pygame.draw.rect(windowSurface,C, (300, 700, 100, 100),)
    pygame.draw.rect(windowSurface,C, (300, 500, 100, 100),)
    pygame.draw.rect(windowSurface,C, (300, 300, 100, 100),)

    pygame.draw.rect(windowSurface,C, (200, 00, 100, 100),)
    pygame.draw.rect(windowSurface,C, (200, 600, 100, 100),)
    pygame.draw.rect(windowSurface,C, (200, 400, 100, 100),)
    pygame.draw.rect(windowSurface,C, (200, 200, 100, 100),)

    pygame.draw.rect(windowSurface,C, (100, 100, 100, 100),)
    pygame.draw.rect(windowSurface,C, (100, 700, 100, 100),)
    pygame.draw.rect(windowSurface,C, (100, 500, 100, 100),)
    pygame.draw.rect(windowSurface,C, (100, 300, 100, 100),)

    pygame.draw.rect(windowSurface,C, (000, 00, 100, 100),)
    pygame.draw.rect(windowSurface,C, (000, 600, 100, 100),)
    pygame.draw.rect(windowSurface,C, (000, 400, 100, 100),)
    pygame.draw.rect(windowSurface,C, (000, 200, 100, 100),)


    #DÉBUT DU JEU
    if event.type == MOUSEBUTTONDOWN and event.button==1:
        compteur += 1
        current_pos = cavalier.get_rect()                   #Obtention de la position du cavalier
        print ("current_pos:", current_pos)
        cx = current_pos[0] // 100                          #Transformation en index de la grille
        cy = current_pos[1] // 100
        print("cx:",cx,"cy;",cy)
        mouse_pos = pygame.mouse.get_pos()                  #`Position du clic
        new_x = mouse_pos[0] // 100
        new_y = mouse_pos[1] // 100
        for i in range (len(AVA)):                          #Positions disponibles
            x =  cx + AVA [i][0]
            y =  cy + AVA [i][1]
            print ("x:",x,"y:", y)
            if GRILLE [y][x] == 0 and new_x == x and new_y == y:        #Vérification de toutes les variables nécéssaires
                GRILLE[new_y][new_x] = 1
                current_pos = (new_x * 100, new_y*100)
                windowSurface.blit(cavalier, current_pos)

        print (mouse_pos)

        pygame.display.flip()






pygame.quit()

