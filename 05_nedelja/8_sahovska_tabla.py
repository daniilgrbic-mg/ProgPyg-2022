import pygamebg
import pygame as pg

prozor = pygamebg.open_window(800, 800, "Prazan")

for x in range(0, 701, 100):
    for y in range(0, 701, 100):
        if (x+y) % 200 == 0:
            pg.draw.rect(prozor, pg.Color("white"), (x, y, 100, 100))
        else:
            pg.draw.rect(prozor, pg.Color("black"), (x, y, 100, 100))

pygamebg.wait_loop()