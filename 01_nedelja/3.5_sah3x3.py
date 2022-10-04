import pygamebg
import pygame as pg

prozor = pygamebg.open_window(600, 600, "Prazan")

pg.draw.rect(prozor, pg.Color("white"), (200,0,200,200))  # gornji beli
pg.draw.rect(prozor, pg.Color("white"), (0,200,200,200))  # levi beli
pg.draw.rect(prozor, pg.Color("white"), (400,200,200,200))  # desni beli
pg.draw.rect(prozor, pg.Color("white"), (200,400,200,200))  # donji beli

pygamebg.wait_loop()
