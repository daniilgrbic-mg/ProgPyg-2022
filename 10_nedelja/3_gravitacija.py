"""
Zadatak lici na obicno ubrzano kretanje, samo sto sada menjamo y-koordinatu
"""

import pygame as pg
import pygamebg
from pygame import Vector2

prozor = pygamebg.open_window(800, 800, "PRIMER")

pozicija = 0
brzina = 0
gravitacija = 1

def frejm():
    prozor.fill(pg.Color("white"))

    global pozicija
    global brzina
    pozicija += brzina
    brzina += gravitacija

    pg.draw.circle(prozor, pg.Color("black"), (400, pozicija), 10)
    #                                               ^ menja se samo y-koordinata!


pygamebg.frame_loop(30, frejm)