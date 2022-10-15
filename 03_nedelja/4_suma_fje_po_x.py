import pygamebg
import pygame as pg


def nacrtaj_jelku(x):
    pg.draw.rect(prozor, pg.Color("brown"), (x - 10, 300 - 20, 20, 20))
    pg.draw.polygon(
        prozor,
        pg.Color("green"),
        [(x, 100), (x - 50, 300 - 20), (x + 50, 300 - 20)]
    )


prozor = pygamebg.open_window(400, 400, "Prazan")

nacrtaj_jelku(100)
nacrtaj_jelku(200)
nacrtaj_jelku(300)

pygamebg.wait_loop()
