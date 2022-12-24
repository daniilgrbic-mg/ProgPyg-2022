import pygame as pg
import pygamebg
from pygame import Vector2

prozor = pygamebg.open_window(900, 900, "Rasveta")

avion = pg.image.load("./avion.png")
avion = pg.transform.scale(avion, (100, 100))

pozicija = Vector2(0, 800)
brzina = Vector2(5, -5)

def frejm():
    global pozicija
    pozicija += brzina
    prozor.fill(pg.Color("lightblue")) 
    prozor.blit(avion, pozicija)

pygamebg.frame_loop(30, frejm)