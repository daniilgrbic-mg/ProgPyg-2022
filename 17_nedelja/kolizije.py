import pygamebg
import pygame
from pygame import Vector2, Color, Rect

prozor = pygamebg.open_window(600, 400, 'Kolizije')

pravougaonici = [
    Rect(400, 50, 200, 150),
    Rect(350, 100, 200, 150),
    Rect(15, 200, 50, 200),
    Rect(500, 350, 150, 100),
]

igrac = Vector2(300-20, 200-20)

def obnovi_frejm():
    prozor.fill(Color('white'))

    tasteri = pygame.key.get_pressed()
    if tasteri[pygame.K_LEFT]: 
        igrac.x -= 10
    if tasteri[pygame.K_RIGHT]: 
        igrac.x += 10
    if tasteri[pygame.K_UP]: 
        igrac.y -= 10
    if tasteri[pygame.K_DOWN]: 
        igrac.y += 10

    for p in pravougaonici:
        if p.colliderect((igrac.x, igrac.y, 40, 40)):
            pygame.draw.rect(prozor, Color('green'), p)
        else:
            pygame.draw.rect(prozor, Color('red'), p)

    pygame.draw.rect(prozor, Color('black'), (igrac.x, igrac.y, 40, 40))

def obradi_dogadjaj(dogadjaj):
    pass

pygamebg.frame_loop(30, obnovi_frejm, obradi_dogadjaj)

