import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Taille initiale
size = (800, 600)

# Création de la fenêtre redimensionnable
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption("Fenêtre rouge redimensionnable")


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Print(self):
        print("x =", self.x)
        print("y =", self.y)
        

class Circle:

    def __init__(self, x, y, radius):
        self.position = Point(x, y)
        self.radius = radius

    def Print(self):
        self.position.Print()
        print("radius =", self.radius)

    def Draw(self, screen):
        pygame.draw.circle(screen, (0, 255, 0), (int(self.position.x), int(self.position.y)), self.radius)

my_circles = []

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        elif event.type == pygame.MOUSEBUTTONUP:
            c = Circle(event.pos[0], event.pos[1], 50)
            my_circles.append(c);


        elif event.type == pygame.VIDEORESIZE:
            # Mettre à jour la taille de la fenêtre
            size = event.size
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)

    # Remplissage de l'écran en rouge
    screen.fill((255, 0, 0))

    for c in my_circles:
        c.Draw(screen)

    pygame.display.flip()

# Fermeture propre
pygame.quit()
sys.exit()
