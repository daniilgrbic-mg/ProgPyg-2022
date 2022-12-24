import pygame
import pygamebg
from pygame import Vector2

prozor = pygamebg.open_window(800, 900, "ubrzanje")

poz = Vector2(0, 450)
v = Vector2(50, -50)
g = Vector2(0, 10)
dt = 1
t_proslo = 0

def frejm():
    global poz
    global v
    global t_proslo

    v += g * dt
    poz += v * dt
    t_proslo += dt

    if poz.y <= 900:
        print(t_proslo)

    # prozor.fill(pygame.Color("black"))
    pygame.draw.circle(prozor, pygame.Color("white"), poz, 10)

pygamebg.frame_loop(5, frejm)