import pygamebg
import pygame as pg


def nacrtaj_jelku(x, y):
    pg.draw.rect(prozor, pg.Color("brown"), (x - 10, y - 20, 20, 20))
    pg.draw.polygon(
        prozor,
        pg.Color("green"),
        [(x, y-200), (x - 50, y - 20), (x + 50, y - 20)]
    )


prozor = pygamebg.open_window(400, 400, "Prazan")

nacrtaj_jelku(100, 250)
nacrtaj_jelku(200, 300)
nacrtaj_jelku(300, 350)

pygamebg.wait_loop()
