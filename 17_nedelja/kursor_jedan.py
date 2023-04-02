import pygame
import pygamebg
from pygame import Vector2, Color, Rect

prozor = pygamebg.open_window(800, 600, 'Interakcija')

pravougaonik = Rect(150, 300, 50, 150)

def obnovi_frejm():
    prozor.fill(Color('white'))

    poz_misa = pygame.mouse.get_pos()

    if pravougaonik.collidepoint(poz_misa):
        pygame.draw.rect(prozor, Color('green'), pravougaonik)
    else:
        pygame.draw.rect(prozor, Color('red'), pravougaonik)

def obradi_dgadjaj(dogadjaj):
    pass

pygamebg.frame_loop(60, obnovi_frejm, obradi_dgadjaj)
