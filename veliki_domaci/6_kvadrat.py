import pygame
import pygamebg
from pygame import Vector2

prozor = pygamebg.open_window(800, 800, "Kvadrat")

smer = "DESNO"
pozicija = Vector2(50, 50)

def frejm():
    global smer
    global pozicija

    prozor.fill(pygame.Color("white"))

    if smer == "DESNO":
        pozicija.x += 10
        if pozicija.x == 750:
            smer = "DOLE"
    elif smer == "DOLE":
        pozicija.y += 10
        if pozicija.y == 750:
            smer = "LEVO"
    elif smer == "LEVO":
        pozicija.x -= 10
        if pozicija.x == 50:
            smer = "GORE"
    elif smer == "GORE":
        pozicija.y -= 10
        if pozicija.y == 50:
            smer = "DESNO"
    
    pygame.draw.circle(prozor, pygame.Color("black"), pozicija, 40)
   
pygamebg.frame_loop(100, frejm)