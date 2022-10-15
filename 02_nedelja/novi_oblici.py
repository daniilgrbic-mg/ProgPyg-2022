import pygamebg
import pygame as pg

prozor = pygamebg.open_window(400, 400, "Prazan")

# zuti pravougaonik dimenzija 100x100 (kvadrat), sa gornjim levim temenom u tacki (50,50)
pg.draw.rect(prozor, pg.Color("yellow"), (50, 50, 100, 100), 5)

# crvena elipsa sirine 400 i visine 200, sa gornjim levim temenom (0,0)
pg.draw.ellipse(prozor, pg.Color("red"), (0, 0, 400, 200), 5)

# zeleni mnogougao sa 3 tacke (trougao). Tacke su: (100, 100), (300, 100) i (100, 300)
pg.draw.polygon(
    prozor,
    pg.Color("green"),
    [(100, 100), (300, 100), (100, 300)],
    5
)

pygamebg.wait_loop()
