import pygamebg
import pygame as pg

prozor = pygamebg.open_window(400, 400, "Prazan")

for x in [100, 200, 300]:
    pg.draw.rect(prozor, pg.Color("brown"), (x - 10, 300 - 20, 20, 20))
    pg.draw.polygon(
        prozor,
        pg.Color("green"),
        [(x, 100), (x - 50, 300 - 20), (x + 50, 300 - 20)]
    )

pygamebg.wait_loop()
