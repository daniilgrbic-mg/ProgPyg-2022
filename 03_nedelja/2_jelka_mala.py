import pygamebg
import pygame as pg

prozor = pygamebg.open_window(400, 400, "Prazan")

# sve isto kao i kod jelke sa proslog casa, samo sam malo smanjio dimenzije
pg.draw.rect(prozor, pg.Color("brown"), (200 - 10, 300 - 20, 20, 20))
pg.draw.polygon(
    prozor,
    pg.Color("green"),
    [(200, 100), (200 - 50, 300 - 20), (200 + 50, 300 - 20)]
)

pygamebg.wait_loop()
