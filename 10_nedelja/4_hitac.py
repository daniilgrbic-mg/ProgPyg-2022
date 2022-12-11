import pygame as pg
import pygamebg
from pygame import Vector2

prozor = pygamebg.open_window(800, 800, "PRIMER")
prozor.fill(pg.Color("beige"))

FPS = 60

brojac = 0
pozicija = Vector2(10, 10)
brzina = Vector2(60, 0)
gravitacija = Vector2(0, 9.81)
dt = 0.1

def frejm():
    prozor.fill(pg.Color("beige"))

    global pozicija
    global brzina
    pozicija += brzina * dt
    brzina += gravitacija * dt

    pg.draw.circle(prozor, pg.Color("black"), pozicija, 10)


pygamebg.frame_loop(FPS, frejm)