import pygamebg
import pygame as pg

prozor = pygamebg.open_window(600, 600, "Prazan")

# def nacrtaj_red(y):
#     for x in range(100, 501, 100):
#         pg.draw.circle(prozor, pg.Color("white"), (x, y), 25)

# for y in range(100, 501, 100):
#     nacrtaj_red(y)


for x in range(100, 501, 100):
    for y in range(100, 501, 100):
        pg.draw.circle(prozor, pg.Color("white"), (x, y), 25)

pygamebg.wait_loop()