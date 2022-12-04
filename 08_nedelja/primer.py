import pygame as pg
import pygamebg

prozor = pygamebg.open_window(1000, 600, "PRIMER")
prozor.fill(pg.Color("beige"))

mis1 = pg.image.load("./mis1.png")
mis2 = pg.image.load("./mis2.png")
brojac = 0
x = 0

def frejm():
    prozor.fill(pg.Color("beige"))
    global x
    global brojac
    x += 5
    brojac += 1
    if brojac % 2 == 1:
        prozor.blit(mis1, (x, 0))
    else:
        prozor.blit(mis2, (x, 0))

pygamebg.frame_loop(10, frejm)