import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Taille initiale
size = (800, 600)

# Création de la fenêtre redimensionnable
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption("Fenêtre rouge redimensionnable")

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            # Mettre à jour la taille de la fenêtre
            size = event.size
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)

    # Remplissage de l'écran en rouge
    screen.fill((255, 0, 0))
    pygame.display.flip()

# Fermeture propre
pygame.quit()
sys.exit()
