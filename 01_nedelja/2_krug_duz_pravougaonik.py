import pygamebg
import pygame as pg

prozor = pygamebg.open_window(400, 300, "Prazan")

pg.draw.circle(prozor, pg.Color("green"), (100, 100), 100)
pg.draw.rect(prozor, pg.Color("yellow"), (200, 100, 100, 200))
pg.draw.line(prozor, pg.Color("red"), (0,300), (400,100), 5)

pygamebg.wait_loop()
