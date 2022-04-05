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
bouse_rect = bouse.get_rect()
cavalier_rect = cavalier.get_rect()
compteur = 0

#Variable de la position courrante du cavalier
cx = 0
cy = 0

# Initialisation des parametres
BLCK = 0, 0, 0
WHITE = 255, 255, 255


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
[0,0,0,0,0,0,0,0]]

available= [(-200, 100), (-200, -100), (200, 100), (200, -100), (100, -200), (-100, -200), (100, 200), (-100, 200)]

current_pos = (start)
windowSurface.blit(cavalier, (start))
(cx, cy) = (start)
gri_pos_x = round(cx / 100)
gri_pos_y = round(cy / 100)
GRILLE[gri_pos_y] [gri_pos_x] = 1

pygame.display.flip()


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
    pygame.draw.rect(windowSurface,BLCK, (600, 00, 100, 100),)
    pygame.draw.rect(windowSurface,BLCK, (600, 600, 100, 100),)
    pygame.draw.rect(windowSurface,BLCK, (600, 400, 100, 100),)
    pygame.draw.rect(windowSurface,BLCK, (600, 200, 100, 100),)

    pygame.draw.rect(windowSurface,BLCK, (500, 100, 100, 100),)
    pygame.draw.rect(windowSurface,BLCK, (500, 700, 100, 100),)
    pygame.draw.rect(windowSurface,BLCK, (500, 500, 100, 100),)
    pygame.draw.rect(windowSurface,BLCK, (500, 300, 100, 100),)

    pygame.draw.rect(windowSurface,BLCK, (700, 100, 100, 100),)
    pygame.draw.rect(windowSurface,BLCK, (700, 700, 100, 100),)
    pygame.draw.rect(windowSurface,BLCK, (700, 500, 100, 100),)
    pygame.draw.rect(windowSurface,BLCK, (700, 300, 100, 100),)

    pygame.draw.rect(windowSurface,BLCK, (400, 00, 100, 100),)
    pygame.draw.rect(windowSurface,BLCK, (400, 600, 100, 100),)
    pygame.draw.rect(windowSurface,BLCK, (400, 400, 100, 100),)
    pygame.draw.rect(windowSurface,BLCK, (400, 200, 100, 100),)

    pygame.draw.rect(windowSurface,BLCK, (300, 100, 100, 100),)
    pygame.draw.rect(windowSurface,BLCK, (300, 700, 100, 100),)
    pygame.draw.rect(windowSurface,BLCK, (300, 500, 100, 100),)
    pygame.draw.rect(windowSurface,BLCK, (300, 300, 100, 100),)

    pygame.draw.rect(windowSurface,BLCK, (200, 00, 100, 100),)
    pygame.draw.rect(windowSurface,BLCK, (200, 600, 100, 100),)
    pygame.draw.rect(windowSurface,BLCK, (200, 400, 100, 100),)
    pygame.draw.rect(windowSurface,BLCK, (200, 200, 100, 100),)

    pygame.draw.rect(windowSurface,BLCK, (100, 100, 100, 100),)
    pygame.draw.rect(windowSurface,BLCK, (100, 700, 100, 100),)
    pygame.draw.rect(windowSurface,BLCK, (100, 500, 100, 100),)
    pygame.draw.rect(windowSurface,BLCK, (100, 300, 100, 100),)

    pygame.draw.rect(windowSurface,BLCK, (000, 00, 100, 100),)
    pygame.draw.rect(windowSurface,BLCK, (000, 600, 100, 100),)
    pygame.draw.rect(windowSurface,BLCK, (000, 400, 100, 100),)
    pygame.draw.rect(windowSurface,BLCK, (000, 200, 100, 100),)


    #DÉBUT DU JEU
    if event.type == MOUSEBUTTONDOWN and event.button==1:
        compteur += 1
        mouse_pos = pygame.mouse.get_pos()
        for current_pos in available:
            new_x = current_pos[0] + mouse_pos[0] // 100
            new_y = current_pos[1] + mouse_pos[1] // 100
            current_pos = (new_x * 100, new_y*100)
            windowSurface.blit(cavalier, current_pos)
            pygame.display.flip()
    if compteur >= 64:
        if 0 in GRILLE:
            print("PERDU")
        elif 0 not in GRILLE:
            print("GAGNE")
    print ("Grille:",GRILLE)
    print ("Compteur:", compteur)

pygame.quit()


