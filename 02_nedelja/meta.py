import pygamebg
import pygame as pg

prozor = pygamebg.open_window(400, 400, "Prazan")

pg.draw.circle(prozor, pg.Color("blue"), (200, 200), 150)
pg.draw.circle(prozor, pg.Color("red"), (200, 200), 100)
pg.draw.circle(prozor, pg.Color("yellow"), (200, 200), 50)

pygamebg.wait_loop()
