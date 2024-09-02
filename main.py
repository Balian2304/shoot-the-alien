import pygame
import random
from pgzero.actor import Actor

pygame.init()
WIDTH = 500
HEIGHT = 500
TITLE = "Shoot the Alien!"
pygame.display.set_mode((WIDTH, HEIGHT))
character = Actor('alien')
character.pos = (250, 250)

message = ""

def draw():
    screen.clear()
    screen.fill((255, 0, 0))
    if character:  
        character.draw()
    screen.draw.text(message, center=(250, 80))

def position():
    if character:  
        character.x = random.randint(50, 450)
        character.y = random.randint(50, 450)

def on_mouse_down(pos):
    global message
    if character and character.collidepoint(pos):
        position()
        message = TITLE
    else:
        message = ""  


