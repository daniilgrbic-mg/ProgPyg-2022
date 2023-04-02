import pygame
import pygamebg
from pygame import Vector2, Color

prozor = pygamebg.open_window(800, 600, 'Interakcija')

igrac = Vector2(400, 300)

def obnovi_frejm():
    prozor.fill(Color('white'))

    tasteri = pygame.key.get_pressed()
    if tasteri[pygame.K_LEFT]: 
        igrac.x -= 5
    if tasteri[pygame.K_RIGHT]: 
        igrac.x += 5
    if tasteri[pygame.K_UP]: 
        igrac.y -= 5
    if tasteri[pygame.K_DOWN]: 
        igrac.y += 5

    pygame.draw.circle(prozor, Color('black'), igrac, 40)

def obradi_dgadjaj(dogadjaj):
    pass

pygamebg.frame_loop(60, obnovi_frejm, obradi_dgadjaj)
