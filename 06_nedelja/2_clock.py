import pygame as pg
from pygame import Vector2
import pygamebg

window = pygamebg.open_window(600, 600, "clock")

t = 0

def update():
    global t
    t += 1
    window.fill(pg.Color("black"))
    pg.draw.circle(window, pg.Color("white"), (300, 300), 250)
    pg.draw.line(
        window, 
        pg.Color("red"), 
        (300,300), 
        Vector2(0,-240).rotate(t*6) + Vector2(300,300), 
        10
    )

pygamebg.frame_loop(1, update, None)
