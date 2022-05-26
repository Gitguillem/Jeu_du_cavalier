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
LossSFX.set_volume(0.2)
VicSFX.set_volume(0.7)

# Initialisation de la fenetre
largeur = 800
hauteur = 800
windowSurface = pygame.display.set_mode((largeur, hauteur), 0,32)
pygame.display.set_caption("Jeu du cavalier | Créé par Anthony, Íngrid, Thalia")
pygame.display.set_icon(cavalier)

#Variable de la victoire
gagne = 0

#Variable de la position courrante du cavalier
cx = 0
cy = 0

#Tableau des mouvements du cavalier
AVA = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]

#Tableau des positions où le cavalier a déjà été
used_pos = []

# Initialisation des parametres
BLACK = 0, 0, 0
WHITE = 255, 255, 255
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

#Affichage initial de la grille
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
pygame.draw.rect(windowSurface,BLACK, (600, 000, 100, 100),)
pygame.draw.rect(windowSurface,BLACK, (600, 600, 100, 100),)
pygame.draw.rect(windowSurface,BLACK, (600, 400, 100, 100),)
pygame.draw.rect(windowSurface,BLACK, (600, 200, 100, 100),)

pygame.draw.rect(windowSurface,BLACK, (500, 100, 100, 100),)
pygame.draw.rect(windowSurface,BLACK, (500, 700, 100, 100),)
pygame.draw.rect(windowSurface,BLACK, (500, 500, 100, 100),)
pygame.draw.rect(windowSurface,BLACK, (500, 300, 100, 100),)

pygame.draw.rect(windowSurface,BLACK, (700, 100, 100, 100),)
pygame.draw.rect(windowSurface,BLACK, (700, 700, 100, 100),)
pygame.draw.rect(windowSurface,BLACK, (700, 500, 100, 100),)
pygame.draw.rect(windowSurface,BLACK, (700, 300, 100, 100),)

pygame.draw.rect(windowSurface,BLACK, (400, 000, 100, 100),)
pygame.draw.rect(windowSurface,BLACK, (400, 600, 100, 100),)
pygame.draw.rect(windowSurface,BLACK, (400, 400, 100, 100),)
pygame.draw.rect(windowSurface,BLACK, (400, 200, 100, 100),)

pygame.draw.rect(windowSurface,BLACK, (300, 100, 100, 100),)
pygame.draw.rect(windowSurface,BLACK, (300, 700, 100, 100),)
pygame.draw.rect(windowSurface,BLACK, (300, 500, 100, 100),)
pygame.draw.rect(windowSurface,BLACK, (300, 300, 100, 100),)

pygame.draw.rect(windowSurface,BLACK, (200, 00, 100, 100),)
pygame.draw.rect(windowSurface,BLACK, (200, 600, 100, 100),)
pygame.draw.rect(windowSurface,BLACK, (200, 400, 100, 100),)
pygame.draw.rect(windowSurface,BLACK, (200, 200, 100, 100),)

pygame.draw.rect(windowSurface,BLACK, (100, 100, 100, 100),)
pygame.draw.rect(windowSurface,BLACK, (100, 700, 100, 100),)
pygame.draw.rect(windowSurface,BLACK, (100, 500, 100, 100),)
pygame.draw.rect(windowSurface,BLACK, (100, 300, 100, 100),)

pygame.draw.rect(windowSurface,BLACK, (000, 000, 100, 100),)
pygame.draw.rect(windowSurface,BLACK, (000, 600, 100, 100),)
pygame.draw.rect(windowSurface,BLACK, (000, 400, 100, 100),)
pygame.draw.rect(windowSurface,BLACK, (000, 200, 100, 100),)

#Génération et vérification des positions diponibles:
def positions_dispo():
    dispos = 8                                              # Numéro max de positions disponibles pour le cavalier à un moment
    for i in range (len(AVA)):                              # Création des positions théoriquement disponibles
        rx = cx + AVA[i][0]
        ry = cy + AVA[i][1]
        try:                                                # On essaye de vérifier les positions
            if ry<0 or rx<0:                                # Comme GRILLE est un tableau, il va intérpreter un index de -1 comme la dérnière valeur du tableau, on va donc l'ignorer
                dispos = dispos - 1
            elif GRILLE[ry][rx] == 0:                       # Si la case est disponible, on ne change rien
                dispos = dispos
            elif GRILLE[ry][rx] != 0:                       # Si la case est occupée, on diminue la qté de positions disponibles de 1
                dispos = dispos - 1
        except IndexError:                                  # Si le numéro à un index en dehors des valeurs de la liste (comme -2), on diminue les positions disponibles de 1
            dispos = dispos - 1
    return dispos

def perte():
    dispos = positions_dispo()
    if dispos != 0:                                         # Si il y a plus de 0 positions disponibles, on continue le jeu
        running = True
    elif dispos == 0:                                       # Sinon, on arrête le jeu
        pygame.event.set_blocked(pygame.MOUSEMOTION)        # On arrête l'intérprétation des clicks de la souris
        return dispos

#Vérification de victoire
def victoire():
    if compteur >= 64:                                      # Si le compteur arrive à 64 (seule option pour gagner)
        pygame.event.set_blocked(pygame.MOUSEMOTION)        # On arrête l'intérprétation des clicks de la souris
        gagne = 1
        return gagne


pygame.display.flip()                                       # Mise à jour de l'écran


clock = pygame.time.Clock()
running = True

# Boucle de jeu
while running:
    # Limitation du nombre de tours de boucle par seconde
    clock.tick(60)
    # Boucle des evennements
    for event in pygame.event.get():                        # Si on clique sur la croix pour quitter l'application
        if event.type == pygame.QUIT:
            running = False

    # Dessinage du cavalier
    windowSurface.blit(cavalier, current_pos)

    # Dessinage de la bouse
    for i in range (len(used_pos)):
        windowSurface.blit(bouse, (used_pos[i][0] + 16, used_pos[i][1] + 34))

    # Vérification de perdu ou gagné
    v = victoire()                                          # On obtient les valeurs des variables de perte et victoire
    p = perte()
    if v == 1:                                              # Si on gagne
        pygame.event.set_blocked(pygame.MOUSEMOTION)        # Arrête l'intérprétation des clicks
        windowSurface.blit(game_win, (0, 0))                # Montre l'écran de victoire
        pygame.mixer.music.stop()                           # Arrête la musique de fond
        pygame.mixer.Sound.play(VicSFX)                     # Joue le son de victoire
        pygame.mixer.music.stop()
        pygame.mixer.stop()

    elif p == 0:                                            # Si on perd
        pygame.event.set_blocked(pygame.MOUSEMOTION)
        windowSurface.blit(game_over, (0, 0))
        pygame.mixer.music.stop()
        LossSFX.play(0,3000)
        pygame.mixer.music.stop()


    # Lorsqu'on clique:
    if event.type == MOUSEBUTTONDOWN and event.button==1:
        mouse_pos = pygame.mouse.get_pos()                  # Obtention des coordonnées du click
        old_cords=(cx * 100, cy*100)                        # Transformation des vieilles coordonnées (de la grille) en coordonnées de l'écran
        m_x = mouse_pos[0] // 100                           # Transformation des coordonnées de la souris en coordonnées de la grille
        m_y = mouse_pos[1] // 100
        if GRILLE[m_y][m_x] == 2:                           # Vérification que le carré cliqué ne soit pas déjà occupé
            None
        elif GRILLE[m_y][m_x] == 0:                         # Si le carré cliqué n'est pas déjà occupé
            for i in range (len(AVA)):
                if m_x == cx + AVA[i][0]:                   # Si les coordonnées cliquées correspondent à un des mouvements du cavalier
                    if m_y == cy + AVA[i][1]:
                        GRILLE[cy][cx] = 2                  # Ancien carreau devient occupé
                        used_pos.append(old_cords)          # On ajoute les coordonnées de l'ancien carré à une liste (pour dessiner les bouses)
                        cx = m_x                            # Les coordonnées du cavalier sont changées pour celles où on a cliqué
                        cy = m_y
                        GRILLE[cy][cx] = 1                  # On définit le nouveau carré comme celui utilisé
                        new_pos = (cx * 100 + 18, cy * 100 + 17)    # Positions pour l'affichage du cavalier (avec centration de l'image)
                        current_pos = new_pos
                        compteur += 1                       # On marque le mouvement en augmentant le compteur de 1

                        # Mise à jour des carreaux sur l'écran (élimination des images précédentes)
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
                        pygame.draw.rect(windowSurface,BLACK, (600, 000, 100, 100),)
                        pygame.draw.rect(windowSurface,BLACK, (600, 600, 100, 100),)
                        pygame.draw.rect(windowSurface,BLACK, (600, 400, 100, 100),)
                        pygame.draw.rect(windowSurface,BLACK, (600, 200, 100, 100),)

                        pygame.draw.rect(windowSurface,BLACK, (500, 100, 100, 100),)
                        pygame.draw.rect(windowSurface,BLACK, (500, 700, 100, 100),)
                        pygame.draw.rect(windowSurface,BLACK, (500, 500, 100, 100),)
                        pygame.draw.rect(windowSurface,BLACK, (500, 300, 100, 100),)

                        pygame.draw.rect(windowSurface,BLACK, (700, 100, 100, 100),)
                        pygame.draw.rect(windowSurface,BLACK, (700, 700, 100, 100),)
                        pygame.draw.rect(windowSurface,BLACK, (700, 500, 100, 100),)
                        pygame.draw.rect(windowSurface,BLACK, (700, 300, 100, 100),)

                        pygame.draw.rect(windowSurface,BLACK, (400, 000, 100, 100),)
                        pygame.draw.rect(windowSurface,BLACK, (400, 600, 100, 100),)
                        pygame.draw.rect(windowSurface,BLACK, (400, 400, 100, 100),)
                        pygame.draw.rect(windowSurface,BLACK, (400, 200, 100, 100),)

                        pygame.draw.rect(windowSurface,BLACK, (300, 100, 100, 100),)
                        pygame.draw.rect(windowSurface,BLACK, (300, 700, 100, 100),)
                        pygame.draw.rect(windowSurface,BLACK, (300, 500, 100, 100),)
                        pygame.draw.rect(windowSurface,BLACK, (300, 300, 100, 100),)

                        pygame.draw.rect(windowSurface,BLACK, (200, 000, 100, 100),)
                        pygame.draw.rect(windowSurface,BLACK, (200, 600, 100, 100),)
                        pygame.draw.rect(windowSurface,BLACK, (200, 400, 100, 100),)
                        pygame.draw.rect(windowSurface,BLACK, (200, 200, 100, 100),)

                        pygame.draw.rect(windowSurface,BLACK, (100, 100, 100, 100),)
                        pygame.draw.rect(windowSurface,BLACK, (100, 700, 100, 100),)
                        pygame.draw.rect(windowSurface,BLACK, (100, 500, 100, 100),)
                        pygame.draw.rect(windowSurface,BLACK, (100, 300, 100, 100),)

                        pygame.draw.rect(windowSurface,BLACK, (000, 000, 100, 100),)
                        pygame.draw.rect(windowSurface,BLACK, (000, 600, 100, 100),)
                        pygame.draw.rect(windowSurface,BLACK, (000, 400, 100, 100),)
                        pygame.draw.rect(windowSurface,BLACK, (000, 200, 100, 100),)


    pygame.display.flip()                                   # Mise à jour de l'écran

pygame.quit()
