# Importation de pygame
import pygame

pygame.init()

# Initialisation de la fenetre
largeur = 600
hauteur = 400
windowSurface = pygame.display.set_mode((largeur, hauteur), 0,32)

# Initialisation des parametres

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

    pygame.display.update()

pygame.quit()