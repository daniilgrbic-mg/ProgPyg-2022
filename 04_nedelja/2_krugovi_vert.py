import pygame as pg
import pygamebg

prozor = pygamebg.open_window(400, 400, "2_krugovi_vert.py")

for y in range(100, 301, 50):  # dakle 100, 150, 200, 250 i 300
    pg.draw.circle(prozor, pg.Color("white"), (200, y), 15)

pygamebg.wait_loop()