#Créé le 10/03/2022 à 12:35 CET
#Créé par Anthony, Íngrid et Thalia
#Projet: Jeu du cavalier

#Importation des librairies et initialisation des paramètres
from random import *
from pygame.locals import *
import wave
import pygame
pygame.init()
pygame.mixer.init()

#Son de fond
file_path = 'backgroundSFX.wav'
file_wav = wave.open(file_path)
frequency = file_wav.getframerate()
pygame.mixer.init(frequency=frequency)
pygame.mixer.music.load(file_path)
pygame.mixer.music.play(-1)

# Initialisation des images et sons
game_win = pygame.image.load("GAME_W.jpg")
game_over = pygame.image.load("GAME_OVER.jpg")
bouse = pygame.image.load("bouse.gif")
cavalier = pygame.image.load("cavalier.gif")
VicSFX = pygame.mixer.Sound("VicSFX.wav")
LossSFX = pygame.mixer.Sound("LossSFX.wav")
LossSFX.set_volume(0.7)

# Initialisation de la fenetre
largeur = 800
hauteur = 800
windowSurface = pygame.display.set_mode((largeur, hauteur), 0,32)
pygame.display.set_caption("Jeu du cavalier | Créé par Anthony, Íngrid, Thalia")
pygame.display.set_icon(cavalier)

#Variable de la position courrante du cavalier
cx = 0
cy = 0

#Tableau des mouvements du cavalier
AVA = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]

#Tableau des positions usées
used_pos = []

# Initialisation des parametres
once = 0
BLCK = 0, 0, 0
WHITE = 255, 255, 255
C = BLCK
compteur = 1

# Génération de la position initiale
def start_pos ():
    x = randint(0,7) * 100 + 18
    y = randint(0,7) * 100 + 17
    return x,y
start = start_pos()
current_pos = (start)
(cx, cy) = (start)
current_pos = (cx, cy)

# Définition de la grille de jeu
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

# Position initiale dans la grille
gri_pos_x = round(cx / 100)
gri_pos_y = round(cy / 100)
cx = cx // 100
cy = cy // 100
old_cords = (cx * 100, cy*100)
GRILLE[gri_pos_y] [gri_pos_x] = 1

#Génération et vérification des positions diponibles:
def positions_dispo():
    dispos = 8
    for i in range (len(AVA)):
        rx = cx + AVA[i][0]
        ry = cy + AVA[i][1]
        #print("RX:",rx,"|| RY:",ry)
        try:
            if ry<0 or rx<0:
                dispos = dispos - 1
            elif GRILLE[ry][rx] == 0:
                dispos = dispos
            elif GRILLE[ry][rx] != 0:
                dispos = dispos - 1
        except IndexError:
            dispos = dispos - 1

    return dispos

def check_pos():
    dispos = positions_dispo()
    print(dispos)
    if dispos != 0:
        running = True
    elif dispos == 0:
        running = False
        pygame.event.set_blocked(pygame.MOUSEMOTION)
        windowSurface.blit(game_over, (0, 0))
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(LossSFX)
        pygame.mixer.music.stop()

#Vérification de victoire
def victoire():
    if compteur >= 64:
        running = False
        pygame.event.set_blocked(pygame.MOUSEMOTION)
        windowSurface.blit(game_win, (0, 0))
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(VicSFX)
        pygame.mixer.music.stop()


pygame.display.flip()


# Boucle de jeu
clock = pygame.time.Clock()
running = True


while running:
    # Limitation du nombre de tours de boucle par seconde
    clock.tick(60)
    # Boucle des evennements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # AFFICHAGE DU CADRILLAGE
        # Affichage des carrés blancs:
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

        # Tracer les carrés noirs
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

    # DESSINAGE DU CAVALIER
    windowSurface.blit(cavalier, current_pos)

    # Dessinage de la bouse
    for i in range (len(used_pos)):
        windowSurface.blit(bouse, (used_pos[i][0] + 16, used_pos[i][1] + 34))

    # Lorsqu'on clique:
    if event.type == MOUSEBUTTONDOWN and event.button==1:
        # Vérification de perdu ou gagné
        victoire()
        check_pos()
        mouse_pos = pygame.mouse.get_pos()
        old_cords=(cx * 100, cy*100)
        m_x = mouse_pos[0] // 100
        m_y = mouse_pos[1] // 100
        if GRILLE[m_y][m_x] == 2:
            None
        elif GRILLE[m_y][m_x] == 0:
            for i in range (len(AVA)):
                if m_x == cx + AVA[i][0]:
                    if m_y == cy + AVA[i][1]:
                        GRILLE[cy][cx] = 2
                        used_pos.append(old_cords)
                        cx = m_x
                        cy = m_y
                        GRILLE[cy][cx] = 1
                        new_pos = (cx * 100 + 18, cy * 100 + 17)
                        current_pos = new_pos
                        compteur += 1

    pygame.display.flip()

pygame.quit()
