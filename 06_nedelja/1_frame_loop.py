import pygame as pg
from pygame import Vector2
import pygamebg

window = pygamebg.open_window(600, 600, "pygamebg.frame_loop(...)")

poz = Vector2(0, 150)
v = Vector2(10, 5)

def update():
    global poz
    poz = poz + v
    window.fill(pg.Color("white"))
    pg.draw.circle(window, pg.Color("black"), poz, 25)

pygamebg.frame_loop(30, update, None)
