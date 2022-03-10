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

# Initialisation des parametres
BLCK = 0, 0, 0
WHITE = 255, 255, 255


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


    pygame.display.update()

pygame.quit()