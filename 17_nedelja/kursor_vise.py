import pygame
import pygamebg
from pygame import Vector2, Color, Rect

prozor = pygamebg.open_window(800, 600, 'Interakcija')

pravougaonici = [
    Rect(400, 50, 200, 150),
    Rect(350, 100, 200, 150),
    Rect(15, 200, 50, 200),
    Rect(500, 350, 150, 100),
]

def obnovi_frejm():
    prozor.fill(Color('white'))

    poz_misa = pygame.mouse.get_pos()

    for p in pravougaonici:
        if p.collidepoint(poz_misa):
            pygame.draw.rect(prozor, Color('green'), p)
        else:
            pygame.draw.rect(prozor, Color('red'), p)

def obradi_dgadjaj(dogadjaj):
    pass

pygamebg.frame_loop(60, obnovi_frejm, obradi_dgadjaj)
