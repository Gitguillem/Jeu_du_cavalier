#Créé le 10/03/2022 à 12:35 CET
#Créé par Anthony Presman
#Projet: Jeu du cavalier

# Importation de pygame
import pygame
pygame.init()

# Initialisation de la fenetre
largeur = 800
hauteur = 800
windowSurface = pygame.display.set_mode((largeur, hauteur), 0,32)
bouse = pygame.image.load("bouse.gif")
# Initialisation des parametres
BLCK = 0, 0, 0
WHITE = 255, 255, 255
C = 123, 50, 255


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


    #Affichage des carrés foncés:
    pygame.draw.rect(windowSurface,C, (700, 100, 100, 100),)
    pygame.draw.rect(windowSurface,C, (700, 700, 100, 100),)
    pygame.draw.rect(windowSurface,C, (700, 500, 100, 100),)
    pygame.draw.rect(windowSurface,C, (700, 300, 100, 100),)

    pygame.draw.rect(windowSurface,C, (600, 00, 100, 100),)
    pygame.draw.rect(windowSurface,C, (600, 600, 100, 100),)
    pygame.draw.rect(windowSurface,C, (600, 400, 100, 100),)
    pygame.draw.rect(windowSurface,C, (600, 200, 100, 100),)

    pygame.draw.rect(windowSurface,C, (500, 100, 100, 100),)
    pygame.draw.rect(windowSurface,C, (500, 700, 100, 100),)
    pygame.draw.rect(windowSurface,C, (500, 500, 100, 100),)
    pygame.draw.rect(windowSurface,C, (500, 300, 100, 100),)

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

    pygame.display.update()

pygame.quit()