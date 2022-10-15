import pygamebg
import pygame as pg

prozor = pygamebg.open_window(400, 400, "Prazan")

pg.draw.rect(prozor, pg.Color("blue"), (0, 0, 400, 200))
pg.draw.rect(prozor, pg.Color("green"), (0, 200, 400, 200))

pg.draw.circle(prozor, pg.Color("yellow"), (350, 50), 40)

pg.draw.rect(prozor, pg.Color("brown"), (180, 150, 40, 100))
pg.draw.rect(prozor, pg.Color("green"), (150, 50, 100, 100))

pygamebg.wait_loop()
