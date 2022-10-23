import pygame as pg
import pygamebg

def auto(x, y):
    pg.draw.rect(prozor, pg.Color("red"), (x-100,y-75,200,50))
    pg.draw.rect(prozor, pg.Color("red"), (x-50,y-125,100,50))
    pg.draw.circle(prozor, pg.Color("black"), (x-60,y-25), 25)
    pg.draw.circle(prozor, pg.Color("black"), (x+60,y-25), 25)

prozor = pygamebg.open_window(400, 250, "0_auto.py")

prozor.fill(pg.Color("white"))
auto(200,250)

pygamebg.wait_loop()