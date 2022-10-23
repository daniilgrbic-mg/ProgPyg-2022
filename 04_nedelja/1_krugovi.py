import pygame as pg
import pygamebg

prozor = pygamebg.open_window(400, 400, "1_krugovi.py")

for x in range(100, 301, 50):  # dakle 100, 150, 200, 250 i 300
    pg.draw.circle(prozor, pg.Color("white"), (x, 200), 15)

pygamebg.wait_loop()