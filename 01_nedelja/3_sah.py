import pygamebg
import pygame as pg

prozor = pygamebg.open_window(400, 400, "Prazan")

pg.draw.rect(prozor, pg.Color("white"), (200,0,200,200))  # gornji desni
pg.draw.rect(prozor, pg.Color("white"), (0,200,200,200))  # donji levi

pygamebg.wait_loop()
