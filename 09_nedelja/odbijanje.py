import pygame as pg
import pygamebg
from pygame import Vector2

prozor = pygamebg.open_window(800, 800, "4 ZIDA")
prozor.fill(pg.Color("beige"))

mis1 = pg.image.load("./mis1.png")
mis2 = pg.image.load("./mis2.png")
brojac = 0
pozicija = Vector2(0, 400)
brzina = Vector2(11, 7)

def frejm():
    global pozicija
    global brzina
    global brojac

    prozor.fill(pg.Color("beige"))

    pozicija += brzina
    
    if pozicija.x > 800-250 or pozicija.x < -10:
        brzina.x = -brzina.x
    if pozicija.y > 800-160 or pozicija.y < -50:
        brzina.y = -brzina.y

    brojac += 1
    if brojac % 2 == 1:
        prozor.blit(mis1, pozicija)
    else:
        prozor.blit(mis2, pozicija)

pygamebg.frame_loop(30, frejm)